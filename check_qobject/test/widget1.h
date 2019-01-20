#ifndef WIDGET_H

#include <QWidget>

class Widget : public QWidget
{
    Q_OBJECT
public:
    Widget(QWidget* parent = NULL);
};

#endif // !WIDGET_H