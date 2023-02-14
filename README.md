
# なんか回転しながらカッコよく登場させる台座

第10回(2023)ソレコンに応募した下記作の3Dデータです。
<https://www.youtube.com/watch?v=WlGEJsPjpvQ>

## 構成

- ロングストロークソレノイド CH12840062
  - <"https://www.takaha.co.jp/SHOP/ch1284.html">
  - 内部抵抗6.2Ωのタイプ
- 24V電源
  - 4A程度流せる容量のもの
  - (大き目のコンデンサを積めば、電流容量は気にしなくていいかも)
- ソレノイドへの電流をOn/Off制御できる回路
  - 24V,4A程度流せる容量のもの
  - 今回は3.3v駆動できる適当なパワーFETを使いました
- マイコン
  - 今回はm5stickC plusを使いました。
  - 80msだけソレノイドに電流を流す、という制御が出きればなんでもいいです。

# フォルダ構成

- src
  - m5stickC plusのソース
- stl
  - swipe_inner.stl
    - せりあがる台座です。外に螺旋が切られているので、せり出すと同時に回転します。
  - straight_inner.stl
    - せりあがる台座の別versionです。直線状の溝が切られており、真っすぐにせり出します。
  - swipe_outer.stl
    - 上記台座を支える外枠の上側です。
  - under_frame.stl
    - 外枠の下側です。
  - top_table.stl
    - swipe_inner/straight_innerの上部につける板です。ここに射出したい物を乗せます。
  - top_extender.st
    - swipe_outerの上にかぶせる囲いです。見た目を整えるためのもので、無くても動作に影響はありません
  - bottom_link.stl x2
    - 蓋を開くリンク機構の一番下です。ソレノイドに接続する部分となります。
    - 薄い側を互い違いになるようにソレノイドに接続します。
  - side_link_lower_r.stl x2(ミラー)
    - bottom_linkと接続するリンク機構の柱です。
    - 左右でミラー反転して出力する必要があります。
  - side_link_higher.stl x2
    - side_link_lowerに接続する柱です。
    - 3Dプリンタのサイズ制限のために分割しています。アクリルサンデー等で接着します。
  - top_field.stl x2
    - side_link_higherに接続する、蓋の部分になります。
    - ここに射出したモノが乗ります
  - marble_cap.stl x2
    - side_link_higherに被せるキャップです。見た目を整えるためのモノで、無くても動作に影響はありません。
