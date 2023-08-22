# FSAEJ-simulator
Assetto Corsaで使用できる学生フォーミュラ日本大会のMODです．パッケージにはTUAT Formula 2020年度車両(NK16_ICV)と2019年度エンデュランスコース(FSAEJ_Endurance),アクセラレーションコース(FSAEJ_Acceleration)，スキッドパッドコース(FSAEJ_Skidpad)が含まれています．また，InvalidateLap appを用いることでパイロンタッチの回数をカウントすることが可能です.  さらに，MultiLaps appを用いることでスキッドパッドのラップタイム計測が可能です．


![Screenshot_nk16_icv_fsaej_endurance_26-2-121-15-5-39](https://user-images.githubusercontent.com/81402033/112589646-d1942780-8e44-11eb-8bea-9b0e71ca5ab1.jpg)
![名称未設定 1](https://user-images.githubusercontent.com/81402033/118453621-6410c300-b732-11eb-8ae5-e6731c23b377.png)






# インストール方法 -Installation-
## 準備 -Preparation-
  
##### 必須 -Required-
- [Steam](https://store.steampowered.com/about/)
- [Assetto Corsa](https://store.steampowered.com/app/244210/Assetto_Corsa/)
- [Content Manager](https://assettocorsa.club/content-manager.html)
- NK16_ICV (Download from this Github)
- FSAEJ_Endurance (Download from this Github)
- FSAEJ_Acceleration (Download from this Github)
- FSAEJ_Skidpad (Download from this Github)
##### オプション -Option-
- [InvalidateLap app](https://assettocorsamods.net/resources/invalidatelap.192/)(assettocorsamods.netのアカウント登録が必要です)
- [MultiLaps app](https://www.racedepartment.com/downloads/multilaps.4997/)(Racedepartmentのアカウント登録が必要です)
___
## 手順 -Instruction-
### 1. Assetto Corsaのダウンロード
[Steam](https://store.steampowered.com/about/)に登録し，[Assetto Corsa](https://store.steampowered.com/app/244210/Assetto_Corsa/)をダウンロードする．  
**ダウンロードしたら起動し、初回セットアップを行う．** 

### 2. Content Managerのダウンロード 
 [Content Manager](https://assettocorsa.club/content-manager.html)のサイトを開き，下へスクロールすると「Download Lite Version:」の項目が出てくる．  
Download directlyをクリック．（Download from Google DriveでもOK）  
<img src="https://user-images.githubusercontent.com/81402033/113232605-75b01f80-92d8-11eb-8815-62db18d7b553.png" width="800px">

ダウンロードされた`Latest.zip`を解凍すると，`latest`フォルダーの中に`Content Manager.exe`と`ReadMe.txt`が作成される．  
`Content Manager.exe`をダブルクリックすると，Content Managerが起動する．  

[参考]  
Content Managerを起動する際に下のようなメッセージが表示される場合がありますが問題はありませんので、詳細情報→実行をクリックしてください
![image](https://user-images.githubusercontent.com/81402033/113668660-8bb14c00-96ed-11eb-8bd5-74f0083bc422.png)
 

![image](https://user-images.githubusercontent.com/81402033/113233557-78ac0f80-92da-11eb-9887-8931afd3e4e5.png)

### 3. MODデータの導入
[GitHub](https://github.com/JSAE-ARCHIVES/FSAEJ-simulator)から[Releases](https://github.com/JSAE-ARCHIVES/FSAEJ-simulator/releases)をクリックし、Latest releaseマークのついている最新バージョンの`FSAEJ_Endurance.zip` `FSAEJ_Acceleration.zip` `FSAEJ_Skidpad.zip` `NK16_ICV.zip`をダウンロードする． 


![スクリーンショット 2021-05-15 133005](https://user-images.githubusercontent.com/81402033/118347978-12293b00-b582-11eb-8bd1-73e380af0dbb.png)
![スクリーンショット 2021-05-15 130947](https://user-images.githubusercontent.com/81402033/118347981-16555880-b582-11eb-9019-8dad97d062ac.png)

ダウンロードされた各Zipファイルを解凍すると，`FSAEJ_Endurance` `FSAEJ_Acceleration` `FSAEJ_Skidpad` `NK16_ICV` フォルダが作成される．

**[注意]**    
 - **Zipの解凍方法によっては解凍して作成されたフォルダの下層にもう一つフォルダが作成されている場合があります．その場合は下層のフォルダを使用して下さい．**  



#### **●コースMODの導入**   
`FSAEJ_Endurance`フォルダを
`C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\content\tracks`
に配置する．`FSAEJ_Acceleration` `FSAEJ_Skidpad`についても同様．  

![image](https://user-images.githubusercontent.com/81402033/113249515-c84e0380-92f9-11eb-927b-15e82886d767.png)

#### **●車両MODの導入**  
`NK16_ICV`フォルダを
`C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\content\cars`
に配置する．  

![image](https://user-images.githubusercontent.com/81402033/113249459-ace2f880-92f9-11eb-964e-485ecc65d8b8.png)

#### **●パイロンタッチカウントの導入**   

 [Assetto Corsa Mods](https://assettocorsamods.net/)へアクセスし Sign up now! からアカウントの登録をする． 
 
 ![image](https://user-images.githubusercontent.com/81402033/118346980-9d063780-b57a-11eb-96f6-90c61cc283bb.png)  

 ![スクリーンショット 2021-05-15 123253](https://user-images.githubusercontent.com/81402033/118346934-426cdb80-b57a-11eb-9b45-009586ec5a5c.png)  
 
 登録後，[InvalidateLap app](https://assettocorsamods.net/resources/invalidatelap.192/)から，`invalidatelap.zip` をダウンロードする．  
 
![image](https://user-images.githubusercontent.com/81402033/118346677-2d8f4880-b578-11eb-9152-1b019ebc4db1.png)

[注意]
ログイン状態でないと Download Not Available となってしまうのでログインしてください．
![image](https://user-images.githubusercontent.com/81402033/118347026-fd957480-b57a-11eb-8b19-7414a0b83567.png)



zipファイルの解凍後`InvalidateLap`フォルダを
`C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\apps\python`
に配置する． 

![image](https://user-images.githubusercontent.com/81402033/113258290-bcb50980-9306-11eb-8458-bc8723d9c280.png)  

Content Managerを起動し，Settings→ASSETTO CORSA→APPSへ移動．
Invalidate Lapのチェックボックスをにチェックを入れる． 

![image](https://user-images.githubusercontent.com/81402033/113671806-d1701380-96f1-11eb-8668-265e68f49424.png)

Settings→APPSへ移動．  
Allows tyres outを`0`に設定する．  

![image](https://user-images.githubusercontent.com/81402033/118347227-895bd080-b57c-11eb-8c8d-3845c26ded6f.png)

Settings→Custom Shaders Patchへ移動．  
Yes, please をクリックし，Custom Shaders Patchをオンにする．  


`GENERAL PATCH SETTINGS` `TASKBAR` 以外の項目のActiveのチェックボックス外し，オフにする．  

![image](https://user-images.githubusercontent.com/81402033/113673552-1ac16280-96f4-11eb-90d4-77c28f5b1ea8.png)

**[注意]**    
 - **上記が最小構成の推奨設定です．その他のCUSTOM SHADERS PATCHの設定に関しては各自で調べて追加してください．**    
 - **WEATHER FX をActiveにすると色がおかしくなります．**   


  
レーススタート後，右側のタブからInvalidateLapをオンにすると，パイロンタッチがカウントされるようになる．   

![image](https://user-images.githubusercontent.com/81402033/118347422-3d119000-b57e-11eb-9b69-3449e9e10126.png)



**[注意]**    
 - **連続でパイロンを踏んだ時,高速でパイロンを踏んだ時などはカウントできていないことがあります．あくまで目安として使用して下さい．**    
 - **カウント機能とは別に，FFB付きのハンコンを使用している場合，パイロンを踏んだ時に小さなフィードバックがくるように設定しています．カウントと併せてパイロンタッチの参考にしてください．**   

___
## レース設定 -Race settings-　 　
![image](https://user-images.githubusercontent.com/81402033/113675420-4cd3c400-96f6-11eb-9500-dd7e35049885.png)  

[参考]  
Tyre blanketsの横の3点マークをクリックすると，オートシフト，トラクションコントロール，ABS等の設定ができます．
    
**[注意]**    
 - **MODを使用したいときはAssetto CorsaのアプリからではなくContent Managerからレースを始める必要があります．**  
 - **Assetto Corsaの初回セットアップを済ませないとContent Managerは正常に動作しません．**
 - **レースモードはPRACTICE，HOTLAPのみ使用できます．TIME ATTACK等のモードを選択するとエラーが発生します．**  
 - **PRACTICEのStart from:Pitsを選択しレースをスタートすると、ピットガイが地面に埋まっていますがお使いのパソコンは正常です．**  

![image](https://user-images.githubusercontent.com/81402033/113975416-70277c00-987a-11eb-995d-6d53a0acfbd4.png)


___
# 備考 -Notes-   
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />この 作品 は <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">クリエイティブ・コモンズ 表示 - 非営利 - 継承 4.0 国際 ライセンス</a>の下に提供されています．

ただし，本MODの利用・改造等は自由にしていただいて構いません． 

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
管理：[公益社団法人 自動車技術会](https://www.jsae.or.jp/)  
開発：本同直人　村松滉平　柚木　希  
協力：[東京農工大学 TUAT Formula](http://web.tuat.ac.jp/~fsae/)  
不具合等連絡先：jsae.sim.pj@gmail.com
___




  



