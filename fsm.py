from transitions.extensions import GraphMachine
import vlc


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_drink(self, update):
        text = update.message.text
        return text.lower() == 'go to drink'


    
    def is_going_to_food(self, update):
        text = update.message.text
        return text.lower() == 'go to food'

    def is_going_to_play(self, update):
        text = update.message.text;
        return text.lower() == 'go to play'
#############################################################################################################
    def on_enter_drinkname1(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("http://www.i-write.idv.tw/life/info/picture/50lan/50lan-menu3.jpg")
        self.go_back(update)

    def is_going_to_drinkname1(self, update):
        text = update.message.text
        return text.lower() == '五十嵐'

    def on_enter_drinkname2(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("https://farm1.staticflickr.com/338/30779431154_01febc8043_o.png")
        self.go_back(update)     
    def is_going_to_drinkname2(self, update):
        text = update.message.text
        return text.lower() == '鮮茶道'

    def on_enter_drinkname3(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("http://0437024777.54vip.com.tw/upload/store1/user3/images/236/NEW/20120118154510796.jpg")
        self.go_back(update)
     
    def is_going_to_drinkname3(self, update):
        text = update.message.text
        return text.lower() == '茶湯會'

    def on_enter_drinkname4(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("http://i.imgur.com/4JYJ568.jpg")
        self.go_back(update)
     
    def is_going_to_drinkname4(self, update):
        text = update.message.text
        return text.lower() == '一芳'

    def on_enter_drinkname5(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("https://www.walkerland.com.tw/image/845/0/poi/p62635/m22903/d558aafbab826f421de8360a9193e2c32109d73c.jpg")
        self.go_back(update)
     
    def is_going_to_drinkname5(self, update):
        text = update.message.text
        return text.lower() == '大苑子'
##############################################################################################################
    def on_enter_foodname1(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("https://twcoupon.com/images/menu/p_mcdonalds/lunch.jpg")
        self.go_back(update)

    def is_going_to_foodname1(self, update):
        text = update.message.text
        return text.lower() == '麥當勞'

    def on_enter_foodname2(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("https://s3.goodlife.tw/system/att/000/004/813/image/1466423215.png")
        self.go_back(update)     
    def is_going_to_foodname2(self, update):
        text = update.message.text
        return text.lower() == '肯德基'

    def on_enter_foodname3(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("https://pic.pimg.tw/tina890908/1490446448-1424764353_n.jpg?v=1490446507")
        self.go_back(update)
     
    def is_going_to_foodname3(self, update):
        text = update.message.text
        return text.lower() == '丹丹漢堡'

    def on_enter_foodname4(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("http://moonzoearth.000webhostapp.com/flow/3b/F_3b1115e079cd725005e73e1ec6f61e20.jpg")
        self.go_back(update)
     
    def is_going_to_foodname4(self, update):
        text = update.message.text
        return text.lower() == '必勝客'

    def on_enter_foodname5(self, update):
        update.message.reply_text("這是這家店的菜單")
        update.message.reply_photo("http://3.bp.blogspot.com/_7BrcD-br5D8/SAFx9NnrT_I/AAAAAAAAAPY/7BiW4mv8Ifs/s400/達美樂-Pizza披薩-dominos-喜多多-2.jpg")
        self.go_back(update)
     
    def is_going_to_foodname5(self, update):
        text = update.message.text
        return text.lower() == '達美樂'
##############################################################################################################
    def on_enter_zero(self, update):
        instance = vlc.Instance()
        update.message.reply_text("別想了都沒錢還想玩")
        player = instance.media_player_new()
        media = instance.media_new("https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q=別想了都沒錢還想玩")
        player.set_media(media)
        player.play()
        self.go_back(update)
     
    def is_going_to_zero(self, update):
        text = update.message.text
        return text.lower() == '我沒錢'

    def is_going_to_mid(self, update):
        text = update.message.text
        return text.lower() == '五百元左右'

    def on_enter_mid(self, update):
        instance = vlc.Instance()
        update.message.reply_text("你可以把這些錢存下來")
        player = instance.media_player_new()
        media = instance.media_new("https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q=你可以把這些錢存下來")
        player.set_media(media)
        player.play()
        self.go_back(update)

    def is_going_to_high(self, update):
        text = update.message.text
        return text.lower() == '一千元左右'

    def on_enter_high(self, update):
        instance = vlc.Instance()
        update.message.reply_text("你可以把這些錢存下來")
        player = instance.media_player_new()
        media = instance.media_new("https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q=你可以把這些錢存下來")
        player.set_media(media)
        player.play()
        self.go_back(update)
#########################################################################################################################

    def on_enter_drink(self, update):
        update.message.reply_text("你想喝哪一間飲料?")
    
    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_food(self, update):
        update.message.reply_text("你要吃哪一間餐廳?")
    
    def on_enter_play(self, update):
        update.message.reply_text("你想花多少錢在休閒娛樂上")

   
    
    def on_exit_state2(self, update):
        print('Leaving state2')
