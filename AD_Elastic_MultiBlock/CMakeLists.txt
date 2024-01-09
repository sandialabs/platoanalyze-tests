# copy mesh files from current source dir to binary dir
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/3blocks.xml
                 ${CMAKE_CURRENT_BINARY_DIR}/3blocks.xml COPYONLY)
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/../common/3blocks.exo
                 ${CMAKE_CURRENT_BINARY_DIR}/3blocks.exo COPYONLY)
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/amgx.json
                 ${CMAKE_CURRENT_BINARY_DIR}/amgx.json COPYONLY)

set( CONFIG_FILE "3blocks.xml" )
set( RUN_TIME 7.0 )
set( NUM_RUNS 2 )
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

if (PLATOANALYZE_ENABLE_ENGINEMESH)
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
else()
  ## create test
  add_test( NAME ${TEST_NAME}_regression
            COMMAND ${CMAKE_COMMAND}
            -DANALYZE_EXECUTABLE=${CMAKE_BINARY_DIR}/analyze
            -DCONFIG_FILE=${CONFIG_FILE}
            -DOUTPUT_DATA=${OUTPUT_DATA}
            -DGOLD_DATA=${CMAKE_CURRENT_SOURCE_DIR}/gold_data
            -DDIFF_CONF=${CMAKE_CURRENT_SOURCE_DIR}/vtk.diff
            -DDIFF=${VTKDIFF}
            -P ${CMAKE_SOURCE_DIR}/tests/tools/compare.cmake )
endif()
