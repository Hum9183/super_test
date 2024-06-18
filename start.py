# -*- coding: utf-8 -*-
from super_test import darkdragon, main, util

# OK
util.custom_reload(darkdragon)
util.custom_reload(main)

#Error
# util.custom_reload(main)        # ←この時点で古いDarkDragonを取り込む
# util.custom_reload(darkdragon)  # 古いDarkDragonと同一のclassではなくなってしまう

main.main()
