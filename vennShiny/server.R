library(shiny)

# Define server logic required to draw a Venn's plot
shinyServer(function(input, output) {

    output$vennPlot <- renderPlot({
        # data
        # property of the graph
        # draw the plot
    })
})

