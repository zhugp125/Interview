#ifndef WIDGET_H

#include <QWidget>

class Widget : public QWidget
{
public:
    Widget(QWidget* parent = NULL);
};

class Demo : protected QObject
{
    Q_OBJECT
public:
    Demo();
};

#endif // !WIDGET_H