 library(shiny)

 # Define UI for application
 shinyUI(fluidPage(

     # title
     titlePanel("Venn's Diagrams"),


     # Sidebar
     sidebarLayout(
       sidebarPanel(
         selectInput("venntype", "Choose a type of graph:",
                     choices = c("simple", "proportional", "bvenn"))
       ),
       
      # Main Panel
      mainPanel(
        verbatimTextOutput("choice")
      )
   )
))
