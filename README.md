# FSAEJ-simulator
Assetto Corsaで使用できる学生フォーミュラ日本大会のMODです。パッケージにはICV車両(NK16_ICV)とエンデュランスコース(FSAEJ_Endurance)が含まれています。また、InvalidateLap appを用いることでパイロンタッチの回数をカウントすることが可能です。  


![Screenshot_nk16_icv_fsaej_endurance_26-2-121-15-5-39](https://user-images.githubusercontent.com/81402033/112589646-d1942780-8e44-11eb-8bea-9b0e71ca5ab1.jpg)

![preview](https://user-images.githubusercontent.com/81402033/112591112-33ee2780-8e47-11eb-951c-396fc2bc2778.jpg)

# インストール方法 -Installation-
## 準備 -Preparation-
  
##### 必須 -Required-
- [Steam](https://store.steampowered.com/about/)
- [Assetto Corsa](https://store.steampowered.com/app/244210/Assetto_Corsa/)
- [Content Manager](https://assettocorsa.club/content-manager.html)
- NK16_ICV (Download from this Github)
- FSAEJ_Endurance (Download from this Github)
##### オプション -Option-
- InvalidateLap app (Download from this Github)
___
## 手順 -Instruction-
### 1. Assetto Corsaのダウンロード
[Steam](https://store.steampowered.com/about/)に登録し，[Assetto Corsa](https://store.steampowered.com/app/244210/Assetto_Corsa/)をダウンロードする．  
### 2. Content Managerのダウンロード 
 [Content Manager](https://assettocorsa.club/content-manager.html)のサイトを開き，下へスクロールすると「Download Lite Version:」の項目が出てくる．  
Download directlyをクリック．（Download from Google DriveでもOK）  
<img src="https://user-images.githubusercontent.com/81402033/113232605-75b01f80-92d8-11eb-8815-62db18d7b553.png" width="800px">

ダウンロードされた`Latest.zip`を解凍すると，`latest`フォルダーの中に`Content Manager.exe`と`ReadMe.txt`が作成される．  
`Content Manager.exe`をダブルクリックすると，Content Managerが起動する．  

**[注意]  
MODを使用したいときはAssetto CorsaのアプリからではなくContent Managerからレースを始める必要があります．**
![image](https://user-images.githubusercontent.com/81402033/113233557-78ac0f80-92da-11eb-9887-8931afd3e4e5.png)

### 3. MODデータの導入
[GitHub](https://github.com/JSAE-ARCHIVES/FSAEJ-simulator)からCode→Download Zipで`FSAEJ-simulator-main.zip`をダウンロードする．download all files from releases.  

![image](https://user-images.githubusercontent.com/81402033/113244556-32fa4180-92f0-11eb-8dc5-1605ab9e4ab2.png)  

ダウンロードされた`FSAEJ-simulator-main.zip`を解凍すると，`FSAEJ_Endurance` `NK16_ICV` `InvalidateLap`フォルダが作成される．  

![image](https://user-images.githubusercontent.com/81402033/113249012-f8e16d80-92f8-11eb-9be0-a269dee9ca43.png)


- コースMODの導入  
`FSAEJ_Endurance`フォルダを
`C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\content\tracks`
に配置する．  

![image](https://user-images.githubusercontent.com/81402033/113249515-c84e0380-92f9-11eb-927b-15e82886d767.png)

- 車両MODの導入  
`NK16_ICV`フォルダを
`C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\content\cars`
に配置する．  

![image](https://user-images.githubusercontent.com/81402033/113249459-ace2f880-92f9-11eb-964e-485ecc65d8b8.png)

- パイロンタッチカウントの導入  
`InvalidateLap`フォルダを
`C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\apps\python`
に配置する． 

![image](https://user-images.githubusercontent.com/81402033/113258290-bcb50980-9306-11eb-8458-bc8723d9c280.png)

Content Managerを起動し，Settings→Custom Shaders Patchへ移動．  
Yes, please をクリックし，Custom Shaders Patchをオンにする．  

![image](https://user-images.githubusercontent.com/81402033/113259074-aeb3b880-9307-11eb-8357-76f1c20c3893.png)

GENERAL PATCH SETTINGS以外の項目のActiveのチェックボックス外し，オフにする．　　

![image](https://user-images.githubusercontent.com/81402033/113260370-27674480-9309-11eb-87de-b7fd7787ca3f.png)

レーススタート後右側のタブからInvalidateLapをオンにすると，パイロンタッチがカウントされるようになる．
**[注意]  
連続でパイロンを踏んだ時などはカウントできていないことがあります．**

![image](https://user-images.githubusercontent.com/81402033/113261374-5a5e0800-930a-11eb-9c3d-c92919dabb69.png)  


___
本MODの利用・改造等は自由にしていただいて構いません．  

FSAE関連のMODを以下にまとめました．動作は確認していません． 

- FSAE Car   
[Formula Student UCM 2016](https://www.racedepartment.com/downloads/formula-student-ucm-2016.19272/) - EV  
[MAD Formula Team MFTC3](https://www.racedepartment.com/downloads/mad-formula-team-mftc3.36690/) - ICV  
[FSAE: Monash Motorsport M17c](https://www.racedepartment.com/downloads/fsae-monash-motorsport-m17c.35841/) - ICV  

- FSAE Track  
[Formula Student UK 2020 - Sprint](https://www.racedepartment.com/downloads/formula-student-uk-2020-sprint.34588/)  
[FSAE: Netball Court Autocross](https://www.racedepartment.com/downloads/fsae-netball-court-autocross.17593/)  
[FSAE: Michigan - AutoX '18](https://www.racedepartment.com/downloads/fsae-michigan-autox-18-beta.21013/)  

- Mini Circuit  
[AC GPK Albert Park](https://www.racedepartment.com/downloads/ac-gpk-albert-park.39655/)  
[AC GPK Barcelona](https://www.racedepartment.com/downloads/ac-gpk-barcelona.39628/)   
[AC GPK Spa](https://www.racedepartment.com/downloads/ac-gpk-spa.39627/)  
[AC GPK Bahrain](https://www.racedepartment.com/downloads/ac-gpk-bahrain.40201/)  

___
作成：[公益社団法人 自動車技術会](https://www.jsae.or.jp/)   
協力：[東京農工大学 TUAT Formula](http://web.tuat.ac.jp/~fsae/)  
不具合等連絡先：jsae.sim.pj@gmail.com
___




  



