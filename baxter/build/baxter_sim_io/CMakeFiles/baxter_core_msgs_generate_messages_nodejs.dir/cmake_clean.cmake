file(REMOVE_RECURSE
  "baxter_sim_io_automoc.cpp"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/baxter_core_msgs_generate_messages_nodejs.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
