#include "FileServer.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    FileServer w;
    w.show();

    return a.exec();
}
