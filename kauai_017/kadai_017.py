#名前(name)と年齢(age)の属性を持つHumanクラス
class Human:
  def __init__ (self, name, age):
    self.name = name
    self.age = age
  
  #大人かどうか判定するcheck_adultメソッド
  def check_adult(self):
    if self.age >= 20:
      print("私は大人です。")
    else:
      print("私は大人ではありません。")

#Humanクラスのインスタンスを複数生成
taro = Human("寺子屋　太郎", 36)
jiro = Human("寺子屋　二郎", 24)
saburo = Human("寺子屋　三郎", 14)

#リストに追加
humans = [taro, jiro, saburo]

#リストの要素数分だけcheck_adultメソッドを呼び出し
for human in humans:
  human.check_adult()

