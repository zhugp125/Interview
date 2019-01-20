#ifndef WIDGET_H

#include <QWidget>

class Widget : public QWidget
{
public:
    Widget(QWidget* parent = NULL);

Q_SIGNALS:
    void clicked();
};

#endif // !WIDGET_H