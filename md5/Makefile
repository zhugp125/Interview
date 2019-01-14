#
# Net Library Makefile
#
#
PROGRAM = libmd5.a
SOURCE  = $(wildcard *.cpp)
OBJS 	= $(patsubst %.cpp,%.o, $(SOURCE)) 
%.o: %.cpp
	$(CXX) -c $(BUILD_INCS) $(FORCE_INCLUDE) -o $@ $?

$(PROGRAM):$(OBJS)
	ar -cr $(BUILD_OUT_DIR)/$@ $(OBJS)
	ranlib $(BUILD_OUT_DIR)/$@

clean:
	rm -f $(OBJS) $(BUILD_OUT_DIR)/$(PROGRAM)

