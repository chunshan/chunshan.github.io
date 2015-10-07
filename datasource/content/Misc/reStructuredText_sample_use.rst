reStructuredText的使用试验
=================================

:date: 2015-09-24
:tags: reStructuredText
:slug: restructuredtext_de_shi_yong_shi_yan
:authors: Chunshan
:summary: reStructuredText使用实验

.. contents::
..
   1  Head 1
   2  Head 2
   3  head 3

这是在Github上建站后的第二篇文章，这篇文章用于展示reStructuredText的一些基本用法，如标题，图片，表格，数学公式等，实验之后再用到博客其他文章中。

标题
_____
===============================
Conservation of mass and energy
===============================

文字样式
________

斜体  *I Love Shanghai*

粗体  **I Love Shanghai**


列表
_______

1. 第一条

#. 第二条

   1. 小条

#. 第三条

嵌入程序代码
______________
.. code-block:: python
    :linenos:

    def foo():
        print "Love Python, Love FreeDome"
        print "E文标点,.0123456789,中文标点,. "

表格
______
.. list-table:: Frozen Delights!
  :widths: 15 10 30
  :header-rows: 1

  * - Treat
    - Quantity
    - Description
  * - Albatross
    - 2.99
    - On a stick!
  * - Crunchy Frog
    - 1.49
    - If we took the bones out, it wouldn't be
      crunchy, now would it?
  * - Gannet Ripple
    - 1.99
    - On a stick!

图片
______
 .. figure:: http://www.mri-q.com/uploads/3/2/7/4/3274160/4670936_orig.gif?355

   Simple model of regional circulation

超链接
______
Paul Allen Tipler, Ralph A. Llewellyn (2003-01), `"Modern Physics" <http://books.google.com/?id=tpU18JqcSNkC&lpg=PP1&pg=PA87#v=onepage&q=>`_, W. H. Freeman and Company, pp. 87–88, ISBN `0-7167-4345-0 <http://en.wikipedia.org/wiki/Special:BookSources/0-7167-4345-0>`_
