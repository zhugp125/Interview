#
# array__test
#

PROGRAM = array_test
SRCS = $(wildcard *.cpp)
OBJS = $(patsubst %.cpp, %.o, $(SRCS))

BULID_OUT_DIR = .

# $? 比目标还新的依赖文件列表
%.o: %.cpp
	$(CXX) -c $(INCLUDES) -o $@ $? -std=c++11

# $@ 目标名
# $^ 所有的依赖项
$(PROGRAM): $(OBJS)
	$(CXX) -o $(BULID_OUT_DIR)/$@ $^ $(LIBS)

clean:
	rm -f $(OBJS) $(BULID_OUT_DIR)/$(PROGRAM)
