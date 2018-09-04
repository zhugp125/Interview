#ifndef FILESERVER_H
#define FILESERVER_H

#include <QWidget>

class QTextEdit;
class QLineEdit;
class QTcpServer;
class QTcpSocket;
class QFile;
class QPushButton;

class FileServer : public QWidget
{
    Q_OBJECT

public:
    FileServer(QWidget *parent = 0);
    ~FileServer();

protected Q_SLOTS:
    void onSelectFile();
    void onSenderFile();

    void onNewConnection();
    void onReadyRead();

private:
    void createUI();
    QPushButton* createButton(const QString& text, const char* method);

    void sendData();

    QTextEdit* m_textEdit;
    QLineEdit* m_fileNameEdit;
    QFile* m_file;
    QString m_fileName;
    quint64 m_fileSize;
    quint64 m_sendSize;
    QPushButton* m_selectBtn;
    QPushButton* m_senderBtn;
    QTcpServer* m_tcpServer;
    QTcpSocket* m_tcpSocket;
};

#endif // FILESERVER_H
