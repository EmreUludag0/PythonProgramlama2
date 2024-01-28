import pyaudio as pyo

ses = pyo.PyAudio().open(
    format=pyo.paInt16, # sesin bit derinliğini ve kanal sayısını belirler
    channels=1, # ses kaydının kanal sayısını belirler. 
    rate=44100, # ses kaydının örnekleme hızını belirler 
    input=True, # ses kaydının nereden alınacağını belirtir.
)

ses.start_stream()

# Belirlenen süre kadar sesi kaydeder
for i in range(1000):
    data = ses.read(2048)

ses.stop_stream() 

with open("./sesKayitlari", "a") as dosya: 
    dosya.write(data)



        