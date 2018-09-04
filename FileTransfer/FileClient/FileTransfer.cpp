#include "FileTransfer.h"
#include <QLineEdit>
#include <QProgressBar>
#include <QLabel>
#include <QGridLayout>
#include <QTcpSocket>
#include <QSettings>
#include <QFile>
#include <QMessageBox>
#include "../common/common.h"

#define LABEL_WIDTH 60
#define LINEEDIT_WIDTH 200
#define HEIGHT 20

FileTransfer::FileTransfer(QWidget *parent)
    : QWidget(parent)
    , m_fileNameEdit(NULL)
    , m_fileSizeEdit(NULL)
    , m_curSizeEdit(NULL)
    , m_md5Edit(NULL)
    , m_progressBar(NULL)
    , m_tcpSocket(NULL)
    , m_bStart(false)
    , m_file(NULL)
    , m_nCurSize(0)
    , m_nFileSize(0)
{
    createUI();

    QSettings setting(g_config_path, QSettings::IniFormat, this);
    connectServer(setting.value("socket/ip").toString(), setting.value("socket/port").toInt());
}

FileTransfer::~FileTransfer()
{

}

void FileTransfer::onReadyRead()
{
    if (NULL == m_tcpSocket)
    {
        return ;
    }

    QByteArray buf = m_tcpSocket->readAll();
    if (buf.isNull() || buf.isEmpty())
    {
        return ;
    }

    if (m_bStart)
    {
        readHeader(buf);
    }
    else
    {
        wrtieFile(buf);
    }
}

void FileTransfer::connectServer(const QString &ip, const int port)
{
    if(NULL == m_tcpSocket)
    {
        m_tcpSocket = new QTcpSocket(this);
        connect(m_tcpSocket, SIGNAL(readyRead()), this, SLOT(onReadyRead()));
    }
    m_tcpSocket->connectToHost(ip, port);
    m_bStart = true;

    if (NULL == m_file)
    {
        m_file = new QFile(this);
    }
}

void FileTransfer::closeSocket()
{
    if (m_tcpSocket != NULL)
    {
        m_tcpSocket->disconnectFromHost();
        m_tcpSocket->close();
    }
}

void FileTransfer::readHeader(const QByteArray &buf)
{
    m_bStart = false;

    QStringList strList = QString(buf).split(g_separator);
    m_fileNameEdit->setText(strList[0]);
    m_fileSizeEdit->setText(strList[1] + "KB");
    m_md5Edit->setText(strList[2]);

    m_nCurSize = 0;
    m_curSizeEdit->setText("0KB");

    m_nFileSize = m_fileSizeEdit->text().toULongLong();
    m_progressBar->setRange(0, m_nFileSize);
    m_progressBar->setValue(0);

    QString fileName = m_fileNameEdit->text();
    setWindowTitle(QString("接收的文件：[%1:%2KB]").arg(fileName).arg(m_nFileSize));

    // 创建并打开文件
    m_file->setFileName(fileName);
    if (!m_file->open(QIODevice::WriteOnly))
    {
        QMessageBox::warning(this, "提示", "文件创建打开失败", QMessageBox::Ok);
        closeSocket();
        return ;
    }

    //向服务器回执信息
    m_tcpSocket->write(g_sender_header_over);
}

void FileTransfer::wrtieFile(const QByteArray &buf)
{
    qint64 len = m_file->write(buf);
    m_nCurSize += len;

    m_curSizeEdit->setText(QString("%1KB").arg(m_nCurSize));
    m_progressBar->setValue(m_nCurSize);

    if (m_nCurSize >= m_nFileSize)
    {
        m_file->close();

        m_tcpSocket->write(g_sender_file_over);
        closeSocket();

        if (checkMd5())
        {
            QMessageBox::information(this, "提示", "文件接收完毕", QMessageBox::Ok);
        }
        else
        {
            QMessageBox::information(this, "提示", "MD5校验失败，接收文件与源文件不一致", QMessageBox::Ok);
        }
    }
}

bool FileTransfer::checkMd5()
{
    std::string fileName = m_fileNameEdit->text().toStdString();
    return getMd5ByFile(fileName) == m_md5Edit->text().toStdString();
}

void FileTransfer::createUI()
{
    m_fileNameEdit = createLineEdit();
    m_fileSizeEdit = createLineEdit();
    m_curSizeEdit = createLineEdit();
    m_md5Edit = createLineEdit();

    m_progressBar = new QProgressBar(this);
    m_progressBar->setFixedWidth(LINEEDIT_WIDTH);
    m_progressBar->setValue(0);

    QGridLayout* mainLayout = new QGridLayout(this);
    int nRow = 0;
    mainLayout->addWidget(createLabel("文件名："), nRow, 0, 1, 1, Qt::AlignRight);
    mainLayout->addWidget(m_fileNameEdit, nRow, 1, 1, 2, Qt::AlignLeft);
    ++nRow;
    mainLayout->addWidget(createLabel("文件大小："), nRow, 0, 1, 1, Qt::AlignRight);
    mainLayout->addWidget(m_fileSizeEdit, nRow, 1, 1, 2, Qt::AlignLeft);
    ++nRow;
    mainLayout->addWidget(createLabel("已接收大小："), nRow, 0, 1, 1, Qt::AlignRight);
    mainLayout->addWidget(m_curSizeEdit, nRow, 1, 1, 2, Qt::AlignLeft);
    ++nRow;
    mainLayout->addWidget(createLabel("MD5："), nRow, 0, 1, 1, Qt::AlignRight);
    mainLayout->addWidget(m_md5Edit, nRow, 1, 1, 2, Qt::AlignLeft);
    ++nRow;
    mainLayout->addWidget(createLabel("进度："), nRow, 0, 1, 1, Qt::AlignRight);
    mainLayout->addWidget(m_progressBar, nRow, 1, 1, 2, Qt::AlignLeft);
}

QLabel *FileTransfer::createLabel(const QString &text)
{
    QLabel* label = new QLabel(text, this);
    label->setFixedWidth(LABEL_WIDTH);
    label->setFixedHeight(HEIGHT);

    return label;
}

QLineEdit *FileTransfer::createLineEdit()
{
    QLineEdit* lineEdit = new QLineEdit(this);
    lineEdit->setReadOnly(true);
    lineEdit->setFixedWidth(LINEEDIT_WIDTH);
    lineEdit->setFixedHeight(HEIGHT);

    return lineEdit;
}
