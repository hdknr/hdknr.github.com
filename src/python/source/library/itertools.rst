
:mod:`itertools` --- 効率的なループ実行のためのイテレータ生成関数
=================================================================

.. module:: itertools
   :synopsis: 効率的なループ実行のためのイテレータ生成関数。
.. moduleauthor:: Raymond Hettinger <python@rcn.com>
.. sectionauthor:: Raymond Hettinger <python@rcn.com>

.. testsetup::

   from itertools import *

.. versionadded:: 2.3

.. contents::
    :local:

このモジュールではイテレータ(:term:`iterator`)を構築する部品を実装しています。
プログラム言語 APL, Haskell, SML からアイデアを得ていますが、
Python に適した形に修正されています。

このモジュールは、高速でメモリ効率に優れ、
単独でも組合せても使用することのできるツールを標準化したものです。
同時に、このツール群は "イテレータの代数" を構成していて、 pure Python
で簡潔かつ効率的なツールを作れるようにしています。

例えば、SML の作表ツール ``tabulate(f)`` は ``f(0), f(1), ...``
のシーケンスを作成します。
同じことを Python では :func:`imap` と :func:`count` を組合せて
``imap(f, count())`` という形で実現できます。

これらのツールと、対をなすビルトインの組合せは、 :mod:`operator` モジュール\
にある高速な関数を使うことでうまく実現できます。
例えば、乗算演算子を二つのベクタにmapすることで効率的なドット積ができます:
``sum(imap(operator.mul, vector1, vector2))``

**無限イテレータ:**
----------------------------

==================  =================       =================================================               =========================================
イテレータ          引数                    結果                                                            例
==================  =================       =================================================               =========================================
:func:`count`       start, [step]           start, start+step, start+2*step, ...                            ``count(10) --> 10 11 12 13 14 ...``
:func:`cycle`       p                       p0, p1, ... plast, p0, p1, ...                                  ``cycle('ABCD') --> A B C D A B C D ...``
:func:`repeat`      elem [,n]               elem, elem, elem, ... 無限もしくは n 回                         ``repeat(10, 3) --> 10 10 10``
==================  =================       =================================================               =========================================

**一番短い入力シーケンスで止まるイテレータ:**
--------------------------------------------------------

====================    ============================    ===================================================   =============================================================
イテレータ              引数                            結果                                                  例
====================    ============================    ===================================================   =============================================================
:func:`chain`           p, q, ...                       p0, p1, ... plast, q0, q1, ...                        ``chain('ABC', 'DEF') --> A B C D E F``
:func:`compress`        data, selectors                 (d[0] if s[0]), (d[1] if s[1]), ...                   ``compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F``
:func:`dropwhile`       pred, seq                       seq[n], seq[n+1], pred が偽の場所から始まる           ``dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1``
:func:`groupby`         iterable[, keyfunc]             keyfunc(v) の値でグループ化したサブイテレータ
:func:`ifilter`         pred, seq                       pred(elem) が真になるseqの要素                        ``ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9``
:func:`ifilterfalse`    pred, seq                       pred(elem) が偽になるseqの要素                        ``ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8``
:func:`islice`          seq, [start,] stop [, step]     seq[start:stop:step]                                  ``islice('ABCDEFG', 2, None) --> C D E F G``
:func:`imap`            func, p, q, ...                 func(p0, q0), func(p1, q1), ...                       ``imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000``
:func:`starmap`         func, seq                       func(\*seq[0]), func(\*seq[1]), ...                   ``starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000``
:func:`tee`             it, n                           it1, it2 , ... itn  一つのイテレータを n 個に分ける
:func:`takewhile`       pred, seq                       seq[0], seq[1], pred が偽になるまで                   ``takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4``
:func:`izip`            p, q, ...                       (p[0], q[0]), (p[1], q[1]), ...                       ``izip('ABCD', 'xy') --> Ax By``
:func:`izip_longest`    p, q, ...                       (p[0], q[0]), (p[1], q[1]), ...                       ``izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-``
====================    ============================    ===================================================   =============================================================

**組合せジェネレータ:**
----------------------------

==============================================   ====================       =============================================================
イテレータ                                       引数                       結果
==============================================   ====================       =============================================================
:func:`product`                                  p, q, ... [repeat=1]       デカルト積、ネストしたforループと等価
:func:`permutations`                             p[, r]                     長さrのタプル列, 繰り返しを許さない順列
:func:`combinations`                             p, r                       長さrのタプル列, 繰り返しを許さない組合せ
:func:`combinations_with_replacement`            p, r                       長さrのタプル列, 繰り返しを許した組合せ
``product('ABCD', repeat=2)``                                               ``AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD``
``permutations('ABCD', 2)``                                                 ``AB AC AD BA BC BD CA CB CD DA DB DC``
``combinations('ABCD', 2)``                                                 ``AB AC AD BC BD CD``
``combinations_with_replacement('ABCD', 2)``                                ``AA AB AC AD BB BC BD CC CD DD``
==============================================   ====================       =============================================================


.. _itertools-functions:

Itertool関数
------------

以下の関数は全て、イテレータを作成して返します。
無限長のストリームのイテレータを返す関数もあり、
この場合にはストリームを中断するような関数かループ処理から使用しなければなりません。

chain(\*iterables)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: chain(*iterables)

   先頭の iterable の全要素を返し、
   次に2番目の iterable の全要素…と全 iterable の要素を返すイテレータを作成します。
   連続したシーケンスを、一つのシーケンスとして扱う場合に使用します。
   この関数は以下のスクリプトと同等です： ::

      def chain(*iterables):
          # chain('ABC', 'DEF') --> A B C D E F
          for it in iterables:
              for element in it:
                  yield element


.. classmethod:: chain.from_iterable(iterable)

   もう一つの :func:`chain` のためのコンストラクタです。
   遅延評価される唯一のイテラブル引数から連鎖した入力を受け取ります。
   この関数は以下のコードと等価です： ::

      @classmethod
      def from_iterable(iterables):
          # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
          for it in iterables:
              for element in it:
                  yield element

   .. versionadded:: 2.6

combinations(iterable, r)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: combinations(iterable, r)

   入力 *iterable* の要素からなる長さ *r* の部分列を返します。

   組合せ(combination)は辞書式順序で出力されます。
   したがって、入力 *iterable* がソートされていれば、
   組合せのタプルは整列された形で生成されます。

   各要素は場所に基づいて一意に取り扱われ、値には依りません。
   入力された要素がバラバラならば、各組合せの中に重複した値は現れません。

   この関数は以下のコードと等価です： ::

        def combinations(iterable, r):
            # combinations('ABCD', 2) --> AB AC AD BC BD CD
            # combinations(range(4), 3) --> 012 013 023 123
            pool = tuple(iterable)
            n = len(pool)
            if r > n:
                return
            indices = range(r)
            yield tuple(pool[i] for i in indices)
            while True:
                for i in reversed(range(r)):
                    if indices[i] != i + n - r:
                        break
                else:
                    return
                indices[i] += 1
                for j in range(i+1, r):
                    indices[j] = indices[j-1] + 1
                yield tuple(pool[i] for i in indices)

   :func:`combination` のコードは :func:`permutations` のシーケンスから
   (入力プールでの位置に応じた順序で)
   要素がソートされていないものをフィルターしたようにも表現できます::

        def combinations(iterable, r):
            pool = tuple(iterable)
            n = len(pool)
            for indices in permutations(range(n), r):
                if sorted(indices) == list(indices):
                    yield tuple(pool[i] for i in indices)

   返される要素の数は、 ``0 <= r <= n`` の場合は、 ``n! / r! / (n-r)!``
   で、 ``r > n`` の場合は 0 です。

   .. versionadded:: 2.6

combinations_with_replacement(iterable, r)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: combinations_with_replacement(iterable, r)

   入力 *iterable* から、それぞれの要素が複数回現れることを許して、
   長さ *r* の要素の部分列を返します。

   組合せは、辞書的に並べられた順序で出力されます。
   ですから、入力 *iterable* がソートされていれば、組合せのタプルは
   ソートされた順に生成されます。

   要素は、値ではなく位置に基づいて一意に扱われます。ですから、入力の要素が
   一意であれば、生成された組合せも一意になります。

   以下と等価です::

        def combinations_with_replacement(iterable, r):
            # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
            pool = tuple(iterable)
            n = len(pool)
            if not n and r:
                return
            indices = [0] * r
            yield tuple(pool[i] for i in indices)
            while True:
                for i in reversed(range(r)):
                    if indices[i] != n - 1:
                        break
                else:
                    return
                indices[i:] = [indices[i] + 1] * (r - i)
                yield tuple(pool[i] for i in indices)

   :func:`combinations_with_replacement` のコードは、 :func:`product` の
   部分列から、要素が (入力プールの位置に従って) ソートされた順に
   なっていない項目をフィルタリングしたものとしても表せます::

        def combinations_with_replacement(iterable, r):
            pool = tuple(iterable)
            n = len(pool)
            for indices in product(range(n), repeat=r):
                if sorted(indices) == list(indices):
                    yield tuple(pool[i] for i in indices)

   返される要素の数は、 ``n > 0`` のとき ``(n+r-1)! / r! / (n-1)!`` です。

   .. versionadded:: 2.7

compress(data, selectors)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: compress(data, selectors)

   *data* の要素から、 *selectors* の対応する要素が ``True`` と評価される
   ものだけを返す、フィルタリングしたイテレータを作ります。
   *data* と *selectors* のどちらかが尽きたときに止まります。
   以下と等価です::

       def compress(data, selectors):
           # compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
           return (d for d, s in izip(data, selectors) if s)

   .. versionadded:: 2.7


count(start=0, step=1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: count(start=0, step=1)

   *n* で始まる、等間隔の値を返すイテレータを作成します。
   :func:`imap` で連続したデータの生成によく使われます。
   また、 :func:`izip` にシーケンス番号を追加するのにも使われます。
   この関数は以下のスクリプトと同等です::

      def count(start=0, step=1):
          # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
          n = start
          while True:
              yield n
              n += step

   浮動小数点数で数えるときは、 ``(start + step * i for i in count())``
   のように、掛け算を使ったコードに置き換えたほうが正確にできることがあります。

   .. versionchanged:: 2.7
      *step* 引数を追加し、非整数の引数を取れるようになりました。

.. function:: cycle(iterable)

   iterable から要素を取得し、
   同時にそのコピーを保存するイテレータを作成します。
   iterable の全要素を返すと、セーブされたコピーから要素を返し、
   これを無限に繰り返します。この関数は以下のスクリプトと同等です： ::

      def cycle(iterable):
          # cycle('ABCD') --> A B C D A B C D A B C D ...
          saved = []
          for element in iterable:
              yield element
              saved.append(element)
          while saved:
              for element in saved:
                    yield element

   :func:`cycle` は大きなメモリ領域を使用します。
   使用するメモリ量は iterable の大きさに依存します。


dropwhile(predicate, iterable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: dropwhile(predicate, iterable)

   predicate が真である限りは要素を無視し、
   その後は全ての要素を返すイテレータを作成します。
   このイテレータは、predicate が最初に偽になるまで *全く* 要素を返さないため、
   要素を返し始めるまでに長い時間がかかる場合があります。
   この関数は以下のスクリプトと同等です： ::

      def dropwhile(predicate, iterable):
          # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
          iterable = iter(iterable)
          for x in iterable:
              if not predicate(x):
                  yield x
                  break
          for x in iterable:
              yield x


.. function:: groupby(iterable[, key])

   同じキーをもつような要素からなる *iterable* 中のグループに対して、
   キーとグループを返すようなイテレータを作成します。 *key*
   は各要素に対するキー値を計算する関数です。
   キーを指定しない場合や ``None`` にした場合、
   *key* 関数のデフォルトは恒等関数になり要素をそのまま返します。
   通常、 *iterable* は同じキー関数で並べ替え済みである必要があります。

   :func:`groupby` の操作は Unix の ``uniq`` フィルターと似ています。
   key 関数の値が変わるたびに休止または新しいグループを生成します
   (このために通常同じ key 関数でソートしておく必要があるのです)。
   この動作は SQL の入力順に関係なく共通の要素を集約する GROUP BY とは違ます。

   返されるグループはそれ自体がイテレータで、 :func:`groupby` と
   *iterable* を共有しています。もととなる *iterable* を共有しているため、
   :func:`groupby` オブジェクトの要素取り出しを先に進めると、
   それ以前の要素であるグループは見えなくなってしまいます。
   従って、データが後で必要な場合にはリストの形で保存しておく必要があります： ::

      groups = []
      uniquekeys = []
      data = sorted(data, key=keyfunc)
      for k, g in groupby(data, keyfunc):
          groups.append(list(g))      # Store group iterator as a list
          uniquekeys.append(k)

   :func:`groupby` は以下のコードと等価です： ::

      class groupby(object):
          # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
          # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
          def __init__(self, iterable, key=None):
              if key is None:
                  key = lambda x: x
              self.keyfunc = key
              self.it = iter(iterable)
              self.tgtkey = self.currkey = self.currvalue = object()
          def __iter__(self):
              return self
          def next(self):
              while self.currkey == self.tgtkey:
                  self.currvalue = next(self.it)    # Exit on StopIteration
                  self.currkey = self.keyfunc(self.currvalue)
              self.tgtkey = self.currkey
              return (self.currkey, self._grouper(self.tgtkey))
          def _grouper(self, tgtkey):
              while self.currkey == tgtkey:
                  yield self.currvalue
                  self.currvalue = next(self.it)    # Exit on StopIteration
                  self.currkey = self.keyfunc(self.currvalue)

   .. versionadded:: 2.4


.. function:: ifilter(predicate, iterable)

   predicate が ``True`` となる要素だけを返すイテレータを作成します。
   *predicate* が ``None`` の場合、値が真であるアイテムだけを返します。
   この関数は以下のスクリプトと同等です： ::

      def ifilter(predicate, iterable):
          # ifilter(lambda x: x%2, range(10)) --> 1 3 5 7 9
          if predicate is None:
              predicate = bool
          for x in iterable:
              if predicate(x):
                  yield x


ifilterfalse(predicate, iterable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: ifilterfalse(predicate, iterable)

   predicateが ``False`` となる要素だけを返すイテレータを作成します。
   *predicate* が ``None`` の場合、値が偽であるアイテムだけを返します。
   この関数は以下のスクリプトと同等です： ::

      def ifilterfalse(predicate, iterable):
          # ifilterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
          if predicate is None:
              predicate = bool
          for x in iterable:
              if not predicate(x):
                  yield x

imap(function, \*iterables)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: imap(function, *iterables)

   iterables の要素を引数として funtion を呼び出すイテレータを作成します。
   *function* が ``None`` の場合、引数のタプルを返します。
   :func:`map` と似ていますが、
   最短の iterable の末尾まで到達した後は
   ``None`` を補って処理を続行するのではなく、終了します。これは、
   :func:`map` に無限長のイテレータを指定するのは多くの場合誤りですが
   (全出力が評価されてしまうため)、
   :func:`imap` の場合には一般的で役に立つ方法であるためです。
   この関数は以下のスクリプトと同等です： ::

      def imap(function, *iterables):
          # imap(pow, (2,3,10), (5,2,3)) --> 32 9 1000
          iterables = map(iter, iterables)
          while True:
              args = [next(it) for it in iterables]
              if function is None:
                  yield tuple(args)
              else:
                  yield function(*args)


islice(iterable, [start,] stop [, step])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: islice(iterable, [start,] stop [, step])

   iterable から要素を選択して返すイテレータを作成します。
   *start* が0以外であれば、iterable の先頭要素は start に達するまでスキップします。
   以降、 *step* が1以下なら連続した要素を返し、
   1以上なら指定された値分の要素をスキップします。
   *stop* が ``None`` であれば、無限に、
   もしくは iterable の全要素を返すまで値を返します。
   ``None`` 以外ならイテレータは指定された要素位置で停止します。
   通常のスライスと異なり、 *start* 、
   *stop* 、 *step* に負の値を指定する事はできません。
   シーケンス化されたデータから関連するデータを取得する場合
   （複数行からなるレポートで、三行ごとに名前が指定されている場合など）
   に使用します。
   この関数は以下のスクリプトと同等です：  ::

      def islice(iterable, *args):
          # islice('ABCDEFG', 2) --> A B
          # islice('ABCDEFG', 2, 4) --> C D
          # islice('ABCDEFG', 2, None) --> C D E F G
          # islice('ABCDEFG', 0, None, 2) --> A C E G
          s = slice(*args)
          it = iter(xrange(s.start or 0, s.stop or sys.maxint, s.step or 1))
          nexti = next(it)
          for i, element in enumerate(iterable):
              if i == nexti:
                  yield element
                  nexti = next(it)

   *start* が ``None`` ならば、繰返しは0から始まります。
   *step* が ``None`` ならば、ステップは1となります。

   .. versionchanged:: 2.5
      *start* と *step* はデフォルト値として ``None`` を受け付けます。


izip(\*iterables)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: izip(*iterables)

   各 iterable の要素をまとめるイテレータを作成します。
   :func:`zip` に似ていますが、リストではなくイテレータを返します。
   複数のイテレート可能オブジェクトに対して、
   同じ繰り返し処理を同時に行う場合に使用します。
   この関数は以下のスクリプトと同等です： ::

      def izip(*iterables):
          # izip('ABCD', 'xy') --> Ax By
          iterables = map(iter, iterables)
          while iterables:
              yield tuple(map(next, iterables))

   .. versionchanged:: 2.4
      イテレート可能オブジェクトを指定しない場合、
      :exc:`TypeError` 例外を送出する代わりに長さゼロのイテレータを返します。

   イテレート可能オブジェクトの左から右への評価順序は保証されます。
   このことによって、データ列を長さnのグループにまとめる常套句
   ``izip(*[iter(s)]*n)`` が実現可能になります。

   :func:`izip` を長さが不揃いな入力に使うのは、
   残され使われなかった長い方のイテレート可能オブジェクトの値を気にしない時だけにするべきです。
   こういった値が重要ならば :func:`izip_longest` を代わりに使ってください。


izip_longest(\*iterables[, fillvalue])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: izip_longest(*iterables[, fillvalue])

   各 iterable の要素をまとめるイテレータを作成します。
   イテレート可能オブジェクトの長さが不揃いならば、足りない値は *fillvalue*
   で埋められます。最も長いイテレート可能オブジェクトが尽きるまで繰り返されます。
   この関数は以下のコードと等価です： ::

      def izip_longest(*args, **kwds):
          # izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
          fillvalue = kwds.get('fillvalue')
          def sentinel(counter = ([fillvalue]*(len(args)-1)).pop):
              yield counter()         # yields the fillvalue, or raises IndexError
          fillers = repeat(fillvalue)
          iters = [chain(it, sentinel(), fillers) for it in args]
          try:
              for tup in izip(*iters):
                  yield tup
          except IndexError:
              pass

   もしイテラブルの内一つでも潜在的に無限列であれば、
   :func:`izip_longest` 関数の呼出しを呼び出し回数を制限する何か
   (たとえば :func:`islice` や :func:`takewhile`)
   で包むべきです。
   *fillvalue* が指定されない場合のデフォルトは ``None`` です。

   .. versionadded:: 2.6

permutations(iterable[, r])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: permutations(iterable[, r])

   *iterable* の要素からなる長さ *r* の置換(permutation)を次々と返します。

   *r* が指定されないかまたは ``None`` であるならば、
   *r* のデフォルトは *iterable* の長さとなり全ての可能な最長の置換が生成されます。

   置換は辞書式にソートされた順序で吐き出されます。
   したがって入力の *iterable* がソートされていたならば、
   置換のタプルはソートされた状態で出力されます。

   要素は位置に基づいて一意的に扱われ、値に基づいてではありません。
   したがって入力された要素が全て異なっているならば、
   それぞれの置換に重複した要素が現れないことになります。

   以下と等価です： ::

        def permutations(iterable, r=None):
            # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
            # permutations(range(3)) --> 012 021 102 120 201 210
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            if r > n:
                return
            indices = range(n)
            cycles = range(n, n-r, -1)
            yield tuple(pool[i] for i in indices[:r])
            while n:
                for i in reversed(range(r)):
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i+1:] + indices[i:i+1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield tuple(pool[i] for i in indices[:r])
                        break
                else:
                    return

   :func:`permutations` のコードは :func:`product` の列から重複のあるもの
   (それらは入力プールの同じ位置から取られたものです)
   を除外するようにフィルタを掛けたものとしても表現できます： ::

        def permutations(iterable, r=None):
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            for indices in product(range(n), repeat=r):
                if len(set(indices)) == r:
                    yield tuple(pool[i] for i in indices)

   返される要素の数は、 ``0 <= r <= n`` の場合 ``n! / (n-r)!``
   で、 ``r > n`` の場合は 0 です。

   .. versionadded:: 2.6

product(\*iterables[, repeat])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: product(*iterables[, repeat])

   入力イテラブルの直積(Cartesian product)です。

   ジェネレータ式の入れ子 for ループと等価になります。
   たとえば ``product(A, B)`` は ``((x,y) for x in A for y in B)``
   と同じものを返します。

   入れ子ループは走行距離計と同じように右端の要素がイテレーションごとに更新されていきます。
   このパターンは辞書式順序を作り出し、
   入力のイテレート可能オブジェクトたちがソートされていれば、
   直積タプルもソートされた順に吐き出されます。

   イテラブル自身との直積を計算するためには、
   オプションの *repeat* キーワード引数に繰り返し回数を指定します。
   たとえば ``product(A, repeat=4)`` は  ``product(A, A, A, A)``
   と同じ意味です。

   この関数は以下のコードと等価ですが、実際の実装ではメモリ中に中間結果を作りません： ::

       def product(*args, **kwds):
           # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
           # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
           pools = map(tuple, args) * kwds.get('repeat', 1)
           result = [[]]
           for pool in pools:
               result = [x+[y] for x in result for y in pool]
           for prod in result:
               yield tuple(prod)

   .. versionadded:: 2.6


repeat(object[, times])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: repeat(object[, times])

   繰り返し *object* を返すイテレータを作成します。
   *times* を指定しない場合、無限に値を返し続けます。
   :func:`imap` で常に同じオブジェクトを関数の引数として指定する場合に使用します。
   また、 :func:`izip`
   で作成するタプルの定数部分を指定する場合にも使用することもできます。
   この関数は以下のスクリプトと同等です： ::

      def repeat(object, times=None):
          # repeat(10, 3) --> 10 10 10
          if times is None:
              while True:
                  yield object
          else:
              for i in xrange(times):
                  yield object


starmap(function, iterable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: starmap(function, iterable)

   iterables の要素を引数として funtion を呼び出すイテレータを作成します。
   function の引数が単一の iterable にタプルとして格納されている場合("zip済み")、
   :func:`imap` の代わりに使用します。 :func:`imap` と
   :func:`starmap` ではfunctionの呼び出し方法が異なり、
   :func:`imap` は ``function(a,b)`` 、 :func:`starmap` では
   ``function(*c)`` のように呼び出します。
   この関数は以下のスクリプトと同等です： ::

      def starmap(function, iterable):
          # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
          for args in iterable:
              yield function(*args)

   .. versionchanged:: 2.6
       以前のバージョンでは、
       :func:`starmap` は関数の引数がタプルであることが必要でした。
       このバージョンからどんなイテレート可能オブジェクトでも良くなりました。



takewhile(predicate, iterable)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: takewhile(predicate, iterable)

   predicate が真である限り iterable から要素を返すイテレータを作成します。
   この関数は以下のスクリプトと同等です： ::

      def takewhile(predicate, iterable):
          # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
          for x in iterable:
              x = iterable.next()
              if predicate(x):
                  yield x
              else:
                  break


tee(iterable[, n=2])
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. function:: tee(iterable[, n=2])

   一つの *iterable* から *n* 個の独立したイテレータを生成して返します。
   以下のコードと等価になります： ::

        def tee(iterable, n=2):
            it = iter(iterable)
            deques = [collections.deque() for i in range(n)]
            def gen(mydeque):
                while True:
                    if not mydeque:             # when the local deque is empty
                        newval = next(it)       # fetch a new value and
                        for d in deques:        # load it to all the deques
                            d.append(newval)
                    yield mydeque.popleft()
            return tuple(gen(d) for d in deques)

   一度 :func:`tee` でイテレータを分割すると、
   もとの *iterable* を他で使ってはいけません。
   さもなければ、 :func:`tee` オブジェクトの知らない間に
   *iterable* が先の要素に進んでしまうことになります。

   :func:`tee` はかなり大きなメモリ領域を使用するかもしれません
   (使用するメモリ量はiterableの大きさに依存します)。
   一般には、一つのイテレータが他のイテレータよりも先にほとんどまたは全ての要素を消費するような場合には、
   :func:`tee` よりも :func:`list`
   を使った方が高速です。

   .. versionadded:: 2.4


.. _itertools-recipes:

レシピ
------

この節では、既存の itertools を素材としてツールセットを拡張するためのレシピを示します。

iterable 全体を一度にメモリ上に置くよりも、
要素を一つづつ処理する方がメモリ効率上の有利さを保てます。
関数形式のままツールをリンクしてゆくと、
コードのサイズを減らし、一時変数を減らす助けになります。
インタプリタのオーバヘッドをもたらす for ループやジェネレータ(:term:`generator`)
を使わずに、 "ベクトル化された" ビルディングブロックを使うと、高速な処理を実現できます。

.. testcode::

   def take(n, iterable):
       "Return first n items of the iterable as a list"
       return list(islice(iterable, n))

   def tabulate(function, start=0):
       "Return function(0), function(1), ..."
       return imap(function, count(start))

   def consume(iterator, n):
       "Advance the iterator n-steps ahead. If n is none, consume entirely."
       # Use functions that consume iterators at C speed.
       if n is None:
           # feed the entire iterator into a zero-length deque
           collections.deque(iterator, maxlen=0)
       else:
           # advance to the empty slice starting at position n
           next(islice(iterator, n, n), None)

   def nth(iterable, n, default=None):
       "Returns the nth item or a default value"
       return next(islice(iterable, n, None), default)

   def quantify(iterable, pred=bool):
       "Count how many times the predicate is true"
       return sum(imap(pred, iterable))

   def padnone(iterable):
       """Returns the sequence elements and then returns None indefinitely.

       Useful for emulating the behavior of the built-in map() function.
       """
       return chain(iterable, repeat(None))

   def ncycles(iterable, n):
       "Returns the sequence elements n times"
       return chain.from_iterable(repeat(tuple(iterable), n))

   def dotproduct(vec1, vec2):
       return sum(imap(operator.mul, vec1, vec2))

   def flatten(listOfLists):
       "Flatten one level of nesting"
       return chain.from_iterable(listOfLists)

   def repeatfunc(func, times=None, *args):
       """Repeat calls to func with specified arguments.

       Example:  repeatfunc(random.random)
       """
       if times is None:
           return starmap(func, repeat(args))
       return starmap(func, repeat(args, times))

   def pairwise(iterable):
       "s -> (s0,s1), (s1,s2), (s2, s3), ..."
       a, b = tee(iterable)
       next(b, None)
       return izip(a, b)

   def grouper(n, iterable, fillvalue=None):
       "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
       args = [iter(iterable)] * n
       return izip_longest(fillvalue=fillvalue, *args)

   def roundrobin(*iterables):
       "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
       # Recipe credited to George Sakkis
       pending = len(iterables)
       nexts = cycle(iter(it).next for it in iterables)
       while pending:
           try:
               for next in nexts:
                   yield next()
           except StopIteration:
               pending -= 1
               nexts = cycle(islice(nexts, pending))

   def powerset(iterable):
       "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
       s = list(iterable)
       return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

   def unique_everseen(iterable, key=None):
       "List unique elements, preserving order. Remember all elements ever seen."
       # unique_everseen('AAAABBBCCDAABBB') --> A B C D
       # unique_everseen('ABBCcAD', str.lower) --> A B C D
       seen = set()
       seen_add = seen.add
       if key is None:
           for element in ifilterfalse(seen.__contains__, iterable):
               seen_add(element)
               yield element
       else:
           for element in iterable:
               k = key(element)
               if k not in seen:
                   seen_add(k)
                   yield element

   def unique_justseen(iterable, key=None):
       "List unique elements, preserving order. Remember only the element just seen."
       # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
       # unique_justseen('ABBCcAD', str.lower) --> A B C A D
       return imap(next, imap(itemgetter(1), groupby(iterable, key)))

   def iter_except(func, exception, first=None):
       """ Call a function repeatedly until an exception is raised.

       Converts a call-until-exception interface to an iterator interface.
       Like __builtin__.iter(func, sentinel) but uses an exception instead
       of a sentinel to end the loop.

       Examples:
           bsddbiter = iter_except(db.next, bsddb.error, db.first)
           heapiter = iter_except(functools.partial(heappop, h), IndexError)
           dictiter = iter_except(d.popitem, KeyError)
           dequeiter = iter_except(d.popleft, IndexError)
           queueiter = iter_except(q.get_nowait, Queue.Empty)
           setiter = iter_except(s.pop, KeyError)

       """
       try:
           if first is not None:
               yield first()
           while 1:
               yield func()
       except exception:
           pass

   def random_product(*args, **kwds):
       "Random selection from itertools.product(*args, **kwds)"
       pools = map(tuple, args) * kwds.get('repeat', 1)
       return tuple(random.choice(pool) for pool in pools)

   def random_permutation(iterable, r=None):
       "Random selection from itertools.permutations(iterable, r)"
       pool = tuple(iterable)
       r = len(pool) if r is None else r
       return tuple(random.sample(pool, r))

   def random_combination(iterable, r):
       "Random selection from itertools.combinations(iterable, r)"
       pool = tuple(iterable)
       n = len(pool)
       indices = sorted(random.sample(xrange(n), r))
       return tuple(pool[i] for i in indices)

   def random_combination_with_replacement(iterable, r):
       "Random selection from itertools.combinations_with_replacement(iterable, r)"
       pool = tuple(iterable)
       n = len(pool)
       indices = sorted(random.randrange(n) for i in xrange(r))
       return tuple(pool[i] for i in indices)

上記のレシピはデフォルト値を指定してグローバルな名前検索をローカル変数の\
検索に変えることで、より効率を上げることができます。
例えば、 *dotproduct* のレシピを書き換えるとすればこんな具合です::

   def dotproduct(vec1, vec2, sum=sum, imap=imap, mul=operator.mul):
       return sum(imap(mul, vec1, vec2))


配列のマージ
^^^^^^^^^^^^^^^

.. testcode::

    >>> itertools.chain(['a', 'b', 'c'], [1, 2, 3])
    <itertools.chain object at 0x5947710>

    >>> list(itertools.chain(['a', 'b', 'c'], [1, 2, 3]))
    ['a', 'b', 'c', 1, 2, 3]
    
    >>> tuple(itertools.chain(['a', 'b', 'c'], [1, 2, 3]))
    ('a', 'b', 'c', 1, 2, 3)
    
