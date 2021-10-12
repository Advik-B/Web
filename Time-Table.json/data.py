# Classes with the links
from json_utils import *
Links = {
    
    'maths':'https://meet.google.com/upa-rhfx-skp',
    # 'hindi':'https://meet.google.com/lookup/hjfyqxgqrb', #NOTE: this hindi is outdated
    'hindi':'https://meet.google.com/lookup/dg3hhit7ov',
    'acp':'https://meet.google.com/lookup/dy2gvdij2t',
    'geogebra':'https://meet.google.com/vqz-pyfs-oed',
    'english':'https://meet.google.com/lookup/aablsrcels',
    'it':'https://meet.google.com/lookup/dtlomler6o',
    'lib':'https://meet.google.com/lookup/bft5sothhe',
    'we':'https://meet.google.com/lookup/derbbdz3ax',
    'sst':'https://meet.google.com/lookup/ge25la4owv',
    'art':'https://meet.google.com/lookup/c6oqic44d6',
    'science':'https://meet.google.com/lookup/a67cm6dfpi',
        
    }

monday = {
    
    '9:00|9:40':['maths', Links['maths'],],
    '10:00|10:40':['english', Links['english']],
    '11:00|11:40':[None, None],
    '12:00|12:40':['it', Links['it']],
    '13:00|13:40':[None, None]
    
    }

tuesday = {
    
    '9:00|9:40':['we', Links['we']],
    '10:00|10:40':['sst', Links['sst']],
    '11:00|11:40':['english', Links['english']],
    '12:00|12:40':['science', Links['science']],
    '13:00|13:40':[None, None],
        
    }

wednesday = {
    
    '9:00|9:40':['maths', Links['maths']],
    '10:00|10:40':['acp', Links['acp']],
    '11:00|11:40':['sst', Links['sst']],
    '12:00|12:40':['science', Links['science']],
    '13:00|13:40':['english', Links['english']],
        
    }

thursday = {
    
    '9:00|9:40':['hindi', Links['hindi']],
    '10:00|10:40':['sst', Links['sst']],
    '11:00|11:40':['science', Links['science']],
    '12:00|12:40':['art', Links['art']],
    '13:00|13:40':[None, None],
        
    }

friday = {
    
    '9:00|9:40':['maths', Links['maths']],
    '10:00|10:40':['english', Links['english']],
    '11:00|11:40':['hindi', Links['hindi']],
    '12:00|12:40':['science', Links['science']],
    '13:00|13:40':[None, None],
        
    }

saturday = {
    
    '9:00|9:40':['hindi', Links['hindi']],
    '10:00|10:40':['sst', Links['sst']],
    '11:00|11:40':['lib', Links['lib']],
    '12:00|12:40':['maths', Links['maths']],
    '13:00|13:40':[None, None],
        
    }

timetable = {
    
    'monday':monday,
    'tuesday':tuesday,
    'wednesday':wednesday,
    'thursday':thursday,
    'friday':friday,
    'saturday':saturday
    
    }
