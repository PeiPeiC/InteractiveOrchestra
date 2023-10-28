import os

scales = {'Major': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '51-4B.wav', '52-5C.wav'],
 'Minor': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '48-4G#.wav', '51-4B.wav', '52-5C.wav'],
  'Blues': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '46-4F#.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav'],
   'Minor pentatonic blues': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav', '57-5F.wav'],
    'Major pentatonic': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '47-4G.wav', '49-4A.wav', '52-5C.wav', '54-5D.wav', '56-5E.wav'],
     'Minor Pentatonic': ['40-4C.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '50-4A#.wav', '52-5C.wav', '55-5D#.wav', '57-5F.wav'],
      'Melodic Minor': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '51-4B.wav', '52-5C.wav'],
       'Dorian Mode': ['40-4C.wav', '42-4D.wav', '43-4D#.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '50-4A#.wav', '52-5C.wav'],
        'Mixolydian Mode': ['40-4C.wav', '42-4D.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '49-4A.wav', '50-4A#.wav', '52-5C.wav'],
         'Ahava Raba Mode': ['40-4C.wav', '41-4C#.wav', '44-4E.wav', '45-4F.wav', '47-4G.wav', '48-4G#.wav', '50-4A#.wav', '52-5C.wav']}

for key, value in scales.items():
    for element in value:
        if not os.path.exists(r"C:\Users\adamf\PycharmProjects\Visual Studio\IO project\InteractiveOrchestra\Test\Violin\\"+element):
            print(f"Not IN: {element}")
            print(key)












