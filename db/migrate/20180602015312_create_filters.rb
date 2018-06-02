class CreateFilters < ActiveRecord::Migration
  def change
    create_table :filters do |t|
      t.string :brand
      t.string :detailurl
      t.string :factory
      t.string :imgname
      t.string :modelname
      t.float :price
      t.string :CA
      t.string :asthma
      t.string :atopy
      t.string :allergy
      t.string :CADR
      t.string :anion
      t.string :compound
      t.string :waterfilter
      t.string :filter
      t.string :varietyfilter
      t.boolean :HEPA
      t.string :PM
      t.float :peoung
      t.string :size

      t.timestamps null: false
    end
  end
end
