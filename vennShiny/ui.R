 library(shiny)

 excel.type  <- c(
     'application/excel',
     'application/vnd.ms-excel',
     '.xls'
 ) 

 # Define UI for application
 shinyUI(fluidPage(

     # title
     titlePanel("Venn's Diagrams"),


     # Sidebar
     sidebarLayout(
       sidebarPanel(
         # Chose what kind of venn graph
         selectInput("venntype", "Choose a type of graph:",
                     choices = c("simple", "proportional", "bvenn"))#,
         #tags$hr(),

         # Insert first file
         #fileInput('file1', 'Choose a file', accept=excel.type),
         #tags$hr()
       ),
       
      # Main Panel
      mainPanel(
        verbatimTextOutput("choice")
      )
   )
))
