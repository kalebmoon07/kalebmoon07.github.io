require 'tzinfo'
require 'tzinfo/data'

TZInfo::DataSource.set(TZInfo::DataSources::RubyDataSource.new)