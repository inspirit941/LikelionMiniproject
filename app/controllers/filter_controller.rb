class FilterController < ApplicationController
  def index
  end
  
  def generic
  end
  
  def elements
  end
  
  
 
  #------------------------가격으로 분류----------------------------------- 

  def low_priced
    @filters = Filter.order(:price).take(10)
    
  end
  
  def standard
    @filters=Filter.find_by_sql("SELECT * FROM filters where price > 140000 AND price < 500000 limit 10")
  end
  
  def premium
    @filters=Filter.find_by_sql("SELECT * FROM filters where price > 500000 limit 10")
  end
  # -------------------------평수로 분류----------------------------------------
  
  
  def one_room
    @filters=Filter.find_by_sql("SELECT * FROM filters where peoung < 10 limit 10")
  end

  def house
    @filters=Filter.find_by_sql("SELECT * FROM filters where peoung > 10 and peoung < 30 limit 10")
  end
  
  def enterprise
    @filters=Filter.find_by_sql("SELECT * FROM filters where peoung > 30 limit 10")
  end
  
  # ----------------------- 미세먼지 박멸--------------------------------------
  
  def dust_killer
    @filters=Filter.find_by_sql("SELECT * FROM filters where length(PM) > 0 limit 10")
  end
  
  
 
end
