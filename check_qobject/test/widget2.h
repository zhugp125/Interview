#ifndef WIDGET_H

#include <QWidget>

class Widget : public QWidget
{
    Q_OBJECT
public:
    Widget(QWidget* parent = NULL);

public slots:
    void onclicked();
};

#endif // !WIDGET_H