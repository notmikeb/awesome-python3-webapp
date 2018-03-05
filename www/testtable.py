import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class Test(Model):
    __table__ = 'test'
    id = StringField(primary_key = True, default = next_id, ddl = 'varchar(50)' )
    name = StringField(default = '', ddl = 'varchar(50)' )
    admin = BooleanField(default = False)
    email = StringField(default = '', ddl = 'varchar(50)' )
    passwd = StringField(default = '', ddl = 'varchar(50)' )

import asyncio
import orm
async def getResult1():
    await orm.create_pool(loop = loop , user = 'www', password = 'www', db = 'awesome')
    t1 = Test(name = 'test1', admin = True)
    await t1.save()
    all = await t1.findAll()
    print( all )

    
if __name__ == "__main__":    
    loop = asyncio.get_event_loop()
    #asyncio.ensure_future(getResult1())
    loop.run_until_complete( getResult1() )
