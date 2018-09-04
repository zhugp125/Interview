#include "FileTransfer.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    FileTransfer w;
    w.show();

    return a.exec();
}
