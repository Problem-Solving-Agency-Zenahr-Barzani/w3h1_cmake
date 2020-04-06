#
# format-clang.rb
# ls src/main.*.c*
# rm src/main.*.c*
# cmake -P compare.cmake
# ruby format-clang.rb
#EXTENSIONS = %w[cxx cpp hpp cu c h]
EXTENSIONS = %w[cxx cpp]
EXTENSIONS.each do |ext|
    puts "ext = #{ext}"
    `clang-format -style=file -i $(find . -name "*.#{ext}")`
end
#