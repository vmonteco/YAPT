FT_PRINTF_PATH=ft_printf
FT_PRINTF_INC_PATH=$(FT_PRINTF_PATH)/includes
LIB_A=$(FT_PRINTF_PATH)/libftprintf.a
LIB_SO=libftprintf.so
PY_TEST=./ft_printf_test.py
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
	FLAGS=--whole-archive
else
	FLAGS=-all_load
endif

all: lib

lib: $(LIB_SO)

$(LIB_SO): $(LIB_A)
	gcc -shared -o $@ -Wl,$(FLAGS) $<

$(LIB_A): FORCE
	make -C $(FT_PRINTF_PATH) all

re: fclean all

clean:
	make -C $(FT_PRINTF_PATH) fclean

fclean: clean
	rm $(LIB_SO)

FORCE:
