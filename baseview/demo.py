
import wda
import time
driver = wda.Client('http://192.168.192.44:8100')
# 跳转POS应用

#IOS 自动化测试，POS op店铺下单的支付流程测试
s= driver.session('com.bindo.pos-beta')

print("测试用例1：华御结setA 套餐计算")
def Payment_process(s):
    s(name='新外卖单').tap()
    time.sleep(2)
    s(name=u'[健康御結] 櫻花蝦醬油拌飯', className='StaticText' ).tap()
    s(name=u'[健康御結] 沖繩風豚肉野菜拌飯', className='StaticText' ).tap()
    s(name=u'北海道牛乳周打蜆湯 S', className='StaticText').tap()
    s(name='Charge').tap()
    s(name='Cash Tender').tap()
    # s(name='好').tap()
    # time.sleep(1)
    # s(name='Cash Tender').tap()
    time.sleep(5)
    s(name='好').tap()
    time.sleep(5)
    s(name='Skip Receipt').tap()
    time.sleep(5)

print("测试用例2：华御结setB 套餐计算")
def Payment_process_1(s):
    s(name='新外卖单').tap()
    time.sleep(2)
    # s(name=u'[健康御結] 櫻花蝦醬油拌飯', className='StaticText' ).tap()
    s(name=u'[健康御結] 沖繩風豚肉野菜拌飯', className='StaticText' ).tap()
    s(name=u'北海道牛乳周打蜆湯 S', className='StaticText').tap()
    s.swipe(0.5, 0.5,0.5,100)
    time.sleep(2)
    s(name=u'京風胡麻春菊', className='StaticText').tap()
    s(name='Charge').tap()
    s(name='Cash Tender').tap()
    # s(name='好').tap()
    # time.sleep(1)
    # s(name='Cash Tender').tap()
    time.sleep(5)
    s(name='好').tap()
    time.sleep(5)
    s(name='Skip Receipt').tap()
    time.sleep(5)

print("测试用例3：华御结setC 套餐计算")
def Payment_process_2(s):
    s(name='新外卖单').tap()
    time.sleep(2)
    s(name=u'[健康御結] 櫻花蝦醬油拌飯', className='StaticText' ).tap()
    s(name=u'[健康御結] 沖繩風豚肉野菜拌飯', className='StaticText' ).tap()
    s(name=u'北海道牛乳周打蜆湯 S', className='StaticText').tap()
    s.swipe(0.5, 0.5, 0.5, 100)
    time.sleep(2)
    s(name=u'京風胡麻春菊', className='StaticText').tap()
    s(name='Charge').tap()
    s(name='Cash Tender').tap()
    # s(name='好').tap()
    # time.sleep(1)
    # s(name='Cash Tender').tap()
    time.sleep(5)
    s(name='好').tap()
    time.sleep(5)
    s(name='Skip Receipt').tap()
    time.sleep(5)

Payment_process(s)
Payment_process_1(s)
Payment_process_2(s)



