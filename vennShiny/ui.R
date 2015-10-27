 library(shiny)

 # Define UI for application
 shinyUI(fluidPage(

     # title
     titlePanel("Venn's Diagrams"),


    # Sidebar
    sidebarLayout(
        sidebarLayout(
            selectInput("kindvenn", "Choose the kind of plot:",
                        choices = c("simple",
                                    "proportional",
                                    "network"))
            # other input
        ),
        # Show a plot
        mainPanel(
            plotOutput("vennPlot")
       )
   )
))
