#include "FileServer.h"
#include <QTextEdit>
#include <QLineEdit>
#include <QPushButton>
#include <QFile>
#include <QFileInfo>
#include <QFileDialog>
#include <QTcpServer>
#include <QTcpSocket>
#include <QSettings>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include "../common/common.h"

#define BUF_SIZE 1024 * 4

FileServer::FileServer(QWidget *parent)
    : QWidget(parent)
    , m_textEdit(NULL)
    , m_fileNameEdit(NULL)
    , m_file(NULL)
    , m_fileSize(0)
    , m_sendSize(0)
    , m_selectBtn(NULL)
    , m_senderBtn(NULL)
    , m_tcpServer(NULL)
    , m_tcpSocket(NULL)
{
    createUI();

    QSettings setting(g_config_path, QSettings::IniFormat, this);
    int port = setting.value("socket/port").toInt();

    m_tcpServer = new QTcpServer(this);
    m_tcpServer->listen(QHostAddress::Any, port);
    connect(m_tcpServer, SIGNAL(newConnection()), this, SLOT(onNewConnection()));

    setWindowTitle(QString("服务器端口：%1").arg(port));
}

FileServer::~FileServer()
{

}

void FileServer::onSelectFile()
{
    QString filePath = QFileDialog::getOpenFileName(this, "打开", "", "");
    if (filePath.isEmpty())
    {
        m_fileNameEdit->setText("无效的路径");
        m_senderBtn->setDisabled(true);
        return ;
    }

    QFileInfo fileInfo(filePath);
    m_fileName = fileInfo.fileName();
    m_fileSize = fileInfo.size();
    m_sendSize = 0;

    m_fileNameEdit->setText(filePath);

    m_senderBtn->setEnabled(true);
}

void FileServer::onSenderFile()
{
    if (NULL == m_tcpSocket)
    {
        return ;
    }

    m_selectBtn->setDisabled(true);
    m_senderBtn->setDisabled(true);

    QString head = m_fileName + g_separator + m_fileSize + g_separator + getMd5ByFile(m_fileName.toStdString()).c_str();
    if (m_tcpSocket->write(head.toUtf8()) < 0)
    {
        m_textEdit->append("文件头部信息发送失败！");
        m_file->close();
    }
}

void FileServer::onNewConnection()
{
    m_tcpSocket = m_tcpServer->nextPendingConnection();
    if(NULL == m_tcpSocket)
    {
        return;
    }

    QString ip = m_tcpSocket->peerAddress().toString();
    quint16 port = m_tcpSocket->peerPort();

    m_textEdit->append(QString("[%1:%2]连接成功").arg(ip).arg(port));
    m_selectBtn->setEnabled(true);

    connect(m_tcpSocket, SIGNAL(readyRead()), this, SLOT(onReadyRead()));
}

void FileServer::onReadyRead()
{
    if(NULL == m_tcpSocket)
    {
        return;
    }

    QByteArray buf = m_tcpSocket->readAll();
    if ("reciver header done" == QString(buf))
    {
        m_textEdit->append("文件头部发送成功，开始发送文件。。。");
        sendData();
    }
    else if ("write file done" == QString(buf))
    {
        m_textEdit->append("开始发送并且接收成功。。。");
        m_file->close();
        m_tcpSocket->disconnectFromHost();
        m_tcpSocket->close();
    }
}

void FileServer::createUI()
{
    m_textEdit = new QTextEdit(this);
    m_textEdit->setReadOnly(true);

    m_fileNameEdit = new QLineEdit(this);
    m_fileNameEdit->setReadOnly(true);

    m_selectBtn = createButton("选择文件", SLOT(onSelectFile()));
    m_senderBtn = createButton("发送文件", SLOT(onSenderFile()));
    m_selectBtn->setDisabled(true);
    m_senderBtn->setDisabled(true);

    QHBoxLayout* hLayout = new QHBoxLayout;
    hLayout->addWidget(m_selectBtn, 0, Qt::AlignLeft);
    hLayout->addWidget(m_fileNameEdit, 1);

    QVBoxLayout* mainLayout = new QVBoxLayout(this);
    mainLayout->addWidget(m_textEdit);
    mainLayout->addLayout(hLayout);
    mainLayout->addWidget(m_senderBtn, 0, Qt::AlignLeft);

    setLayout(mainLayout);
    resize(400, 300);
}

QPushButton *FileServer::createButton(const QString &text, const char *method)
{
    QPushButton* btn = new QPushButton(text, this);
    connect(btn, SIGNAL(clicked(bool)), this, method);

    return btn;
}

void FileServer::sendData()
{
    quint64 len = 0;
    do
    {
        char buf[BUF_SIZE] = {0};
        len = m_file->read(buf, BUF_SIZE);
        len = m_tcpSocket->write(buf, len);

        m_sendSize += len;
    }while(len > 0);
}

