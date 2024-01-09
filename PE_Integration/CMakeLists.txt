# copy mesh files from current source dir to binary dir
  file(COPY        ${CMAKE_CURRENT_SOURCE_DIR}/../PE_Integration
       DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/../)

build_mpi_test_string(ES_MPI_TEST 1 ${CMAKE_BINARY_DIR}/unit_tests/AnalyzeAppIntxTests)
add_test(NAME runAnalyzeAppIntxTests COMMAND ${ES_MPI_TEST})
