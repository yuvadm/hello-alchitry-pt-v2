open_hw_manager
connect_hw_server
puts "Available targets:"
foreach target [get_hw_targets] {
    puts "Target: $target"
}
close_hw_manager
exit