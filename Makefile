SUBDIRS = singleton template strategy

.PHONY: subdirs $(SUBDIRS)

subdirs: $(SUBDIRS)

$(SUBDIRS):
	"$(MAKE)" -C $@
