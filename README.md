class Speaker():
    '''会说话就出本书'''
    def __init__(self,lang='zh',spd='5',per='0',vol='5',pit='5'):
        self.lang=lang
        self.spd=spd
        self.per=per
        self.vol=vol
        self.pit=pit
        
    def speak(self,text=''):
        '''说话啊'''
        wavfile = self.__Spawn_wavfile(text)
        import simpleaudio as sa
        wave_obj = sa.WaveObject.from_wave_file(wavfile)
        play_obj = wave_obj.play()
        play_obj.wait_done()    
        
    def __Spawn_wavfile(self,text,filename='my_audio.wav'):
        '''合成wav文件'''
        from aip import AipSpeech
        APP_ID = '14872735'
        API_KEY = 'B6GuDbyyb8LnGaiGWYY7e1Ma'
        SECRET_KEY = 'qxcHdoBeEcla028wjK8SkGL8gl6sQRUZ'
        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
        options = {'lang' : self.lang, 'spd' : self.spd, 'per' : self.per,
                   'vol' : self.vol, 'pit' : self.pit, 'aue' : 6}
        result = client.synthesis(text,options=options)
        with open(filename,'wb') as f:
            f.write(result)
        return (filename)
    
    def ask(self,question):
        '''语音提问并等待输入'''
        self.speak(question)
        input(question)

                
speaker1=Speaker()
speaker1.ask('现在几点啊？')
