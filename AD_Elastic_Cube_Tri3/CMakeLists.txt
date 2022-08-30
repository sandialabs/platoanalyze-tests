# copy mesh files from current source dir to binary dir
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/cube.xml
                 ${CMAKE_CURRENT_BINARY_DIR}/cube.xml COPYONLY)
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/../common/cube_tri3.exo
                 ${CMAKE_CURRENT_BINARY_DIR}/cube_tri3.exo COPYONLY)
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/amgx.json
                 ${CMAKE_CURRENT_BINARY_DIR}/amgx.json COPYONLY)

set( CONFIG_FILE "cube.xml" )
set( RUN_TIME 3.0 )
set( NUM_RUNS 3 )
set( OUTPUT_DATA "output_data" )

get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
set( TEST_NAME ${testDirName} )

## create test
add_test( NAME ${TEST_NAME}_timing
          COMMAND ${CMAKE_COMMAND}
          -DANALYZE_EXECUTABLE=${CMAKE_BINARY_DIR}/analyze
          -DCONFIG_FILE=${CONFIG_FILE}
          -DRUN_TIME=${RUN_TIME}
          -DNUM_RUNS=${NUM_RUNS}
          -P ${CMAKE_SOURCE_DIR}/tests/tools/timer.cmake )

## create test
add_test( NAME ${TEST_NAME}_regression
          COMMAND ${CMAKE_COMMAND}
          -DANALYZE_EXECUTABLE=${CMAKE_BINARY_DIR}/analyze
          -DCONFIG_FILE=${CONFIG_FILE}
          -DOUTPUT_DATA=${OUTPUT_DATA}.exo
          -DGOLD_DATA=${CMAKE_CURRENT_SOURCE_DIR}/gold_data.exo
          -DDIFF_CONF=${CMAKE_CURRENT_SOURCE_DIR}/exo.diff
          -DDIFF=${EXODIFF}
          -P ${CMAKE_SOURCE_DIR}/tests/tools/compare.cmake )
