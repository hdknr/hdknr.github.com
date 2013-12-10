=======
メモ
=======


処理のパイプライン
======================

sphinx-build.py 実行される
-----------------------------------

from sphinx import main して main() を呼んでsys.exit() して終わり
------------------------------------------------------------------------------------

sphinx.main : from sphinx import cmdline して　cmdline.main() する
------------------------------------------------------------------------------------

cmdline.main: Sphinxのインスタンスを作成してappとし、 app.build()のリターンコードを返して終了。
-------------------------------------------------------------------------------------------------

- from sphinx.application import Sphinx


Spinx._init_ の中で conf.py を処理。
----------------------------------------

- from sphinx.config import Config
- app.config = Config(...)
- app.config.extensions の全てに関して追加(self.setup_extension())
- Config()自体がextensionなので、app.config.setup(app) ( ここにappが渡されるよ！)
- app.config.init_values()
- app._init_i18n()
- app._init_env(freshenv)
- app._init_builder(buildername)

Sphinx.build: 指定されたbuilderに処理依頼。
----------------------------------------------

- app.builder.build_all() / app.builder.build_specific(filenames) / app.builder.build_update() のどれか。
- 最後に app.builder.cleanup()


Config : config_values=dict() に多くの設定値が管理されてる
----------------------------------------------------------------------------

Config.__init__() で初期化
----------------------------------------------------------------------------

- app.conf.values = Config.config_values.copy()
- config = {} を用意して設定
- app.conf.setup = config.get('setup', None) :つまり def setup(app): しておくとSphinxインスタンスもらえるよ！
- app.conf.extensions = config.get('extensions', [])
