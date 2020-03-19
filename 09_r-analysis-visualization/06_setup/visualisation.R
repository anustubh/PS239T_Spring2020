### ------------------------------------------------------------- #
### ---- General Notes ---- 
### ------------------------------------------------------------- #

#' 


### ------------------------------------------------------------- #
### ---- 1. Theme ----
### ------------------------------------------------------------- #

theme_ed_bigtxt <- theme(
  text = element_text(size=16),
  plot.caption = element_text(colour="black",size=10),
  axis.text.y = element_text(colour="black",size=16),
  axis.text.x = element_text(colour="black",size=16),
  legend.text = element_text(colour="black",size=16),
  legend.position = "bottom",
  panel.background = element_rect(fill = NA),
  panel.border = element_rect(fill = NA, color = "grey75"),
  axis.ticks = element_line(color = "grey85"),
  panel.grid.major = element_line(color = "grey95", size = 0.2),
  panel.grid.minor = element_line(color = "grey95", size = 0.2),
  legend.key = element_blank())

theme_ed <- theme(
  legend.position = "bottom",
  panel.background = element_rect(fill = NA),
  panel.border = element_rect(fill = NA, color = "grey75"),
  axis.ticks = element_line(color = "grey85"),
  panel.grid.major = element_line(color = "grey95", size = 0.2),
  panel.grid.minor = element_line(color = "grey95", size = 0.2),
  legend.key = element_blank())

