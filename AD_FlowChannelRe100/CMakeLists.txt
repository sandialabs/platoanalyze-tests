# copy mesh files from current source dir to binary dir
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/flow_rectangular_channel.xml
                 ${CMAKE_CURRENT_BINARY_DIR}/flow_rectangular_channel.xml COPYONLY)
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/flow_rectangular_channel.exo
                 ${CMAKE_CURRENT_BINARY_DIR}/flow_rectangular_channel.exo COPYONLY)
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/amgx.json
                 ${CMAKE_CURRENT_BINARY_DIR}/amgx.json COPYONLY)

set( CONFIG_FILE "flow_rectangular_channel.xml" )
set( RUN_TIME 80 )
set( NUM_RUNS 1 )
set( OUTPUT_DATA "output_data" )

get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
set( TEST_NAME ${testDirName} )

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
