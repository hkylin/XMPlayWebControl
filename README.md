# XMPlayWebControl
Control XMPlay via Web, using Python.

Basically, an HTML5 web app issues ajax request to two python-cgi scripts. One controls the music player,
and the other gets the current title.

You have the basics controls:
Previous, Play/Pause, Stop, Next.
In addition, you can control the volume, and the web app has a time counter. This time counter it's not synchronized with XMPlay,
because it's almost imposible.

The web app is purely HTML5, JS with [Jquery](http://jquery.com/), and CSS with [Bootstrap](http://getbootstrap.com/)

The scripts (these are who do the hard work) are written in [Python](https://www.python.org/), using [python cgi](https://docs.python.org/3.4/library/cgi.html),
and [PyWin32](http://sourceforge.net/projects/pywin32/files/pywin32/).

Basically it's a clean and fresh remake of my previous project [PyRemote XMPlay](https://github.com/lucasdaddiego/pyremote-xmplay).
