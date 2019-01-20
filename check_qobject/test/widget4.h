#ifndef WIDGET_H

#include <QWidget>

class Widget : public QWidget
{
public:
    Widget(QWidget* parent = NULL);

public Q_SLOTS:
    void onclicked();
};

#endif // !WIDGET_H