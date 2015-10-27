 library(shiny)

 # Define UI for application
 shinyUI(fluidPage(

     # title
     titlePanel("Venn's Diagrams"),


    # Sidebar
    SidebarLayout(

        # Show a plot
        mainPanel(
            plotOutput("vennPlot")
       )
   )
))
