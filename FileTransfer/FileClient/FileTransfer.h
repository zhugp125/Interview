#ifndef FILETRANSFER_H
#define FILETRANSFER_H

#include <QWidget>

class QLabel;
class QLineEdit;
class QProgressBar;
class QTcpSocket;
class QFile;

class FileTransfer : public QWidget
{
    Q_OBJECT

public:
    FileTransfer(QWidget *parent = 0);
    ~FileTransfer();

protected Q_SLOTS:
    void onReadyRead();

protected:
    void connectServer(const QString &ip, const int port);
    void closeSocket();

    void readHeader(const QByteArray& buf);
    void wrtieFile(const QByteArray& buf);

    bool checkMd5();

private:
    void createUI();
    QLabel* createLabel(const QString &text);
    QLineEdit* createLineEdit();

    QLineEdit* m_fileNameEdit;
    QLineEdit* m_fileSizeEdit;
    QLineEdit* m_curSizeEdit;
    QLineEdit* m_md5Edit;
    QProgressBar* m_progressBar;

    QTcpSocket* m_tcpSocket;
    bool m_bStart;

    QFile* m_file;
    quint64 m_nCurSize;
    quint64 m_nFileSize;
};

#endif // FILETRANSFER_H
