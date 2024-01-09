# This problem has an analytical solution.  Execute the following in mathematica to get the temperature of the loaded surface, T=535.108774663:
#dsol=DSolve[{y''[x]==0,y'[l]==q-\[Sigma] y[l]^4,y[0]==0},y[x],x];
#SetPrecision[Re[y[x]/.dsol[[4]]/.{q->10000,l->.1,\[Sigma]->5.67*10^-8,x->.1}],12]

# gold_data.exo has a surface temperature of 535.108774663.  

# copy mesh files from current source dir to binary dir
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/block.xml
                 ${CMAKE_CURRENT_BINARY_DIR}/block.xml COPYONLY)
configure_file(  ${CMAKE_CURRENT_SOURCE_DIR}/../common/block.exo
                 ${CMAKE_CURRENT_BINARY_DIR}/block.exo COPYONLY)

set( CONFIG_FILE "block.xml" )
set( RUN_TIME 6.5 )
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
