require 'csv'
namespace :import do
    task :create_database => :environment do
        CSV.foreach("public/aircleaner.csv", encoding: 'utf-8', :headers => true) do |row|
            Filter.create!(row.to_hash)
        end
        puts "Inserting DB complete"
    end
end