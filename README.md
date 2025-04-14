# GIS Analysis and Estimation of a Forest Carbon Stock
QGIS analysis of LiDAR data provided by geoportal.nrw to estimate carbon stocks in the National Park's forests. Combination of Digital Terrain Model (DTM) and Digital Surface Model (DSM) with Enhanced Vegetation Index (EVI) to identify tree heights and derive a Canopy Height Model (CHM).
I combined allometric equations to estimate above-ground carbon in trees by only using the height of the trees. Furhtermore, I included distances to roads and trails to analyze the correlation with tree heights. The resulting map shows where there are carbon hotspots in the forest. The correlation analysis showed no major correlation between road distance and tree height.


## Biomass & Carbon calculation based solely on Height
The primary focus of this project is to showcase and explore different GIS functionalities and potentials in working with LiDAR and remote sensing data. Therefore, a very simple and generalizing approach was chosen to calculate the biomass and hence the final carbon stored in Eifel National Park's forest's trees.
There are several factors, such as age, height, diameter, tree species, canopy density, region, etc. that influence a tree's biomass. In this project,I only used height data, so simplified on those other factors. I combined several species-specific allometric equations (Repola 2009, Cienciala et al. 2005) and generalistic allometric equations (Chave et al. 2014) as well as modelling of the Diameter at Breast Height (DBH) by solely using tree height (Pretzsch 2009).
This leaded to the following formula roughly calculating Above-Ground Biomass (AGB), solely based on tree height (H):

Started with:
I. DBH = exp (−0.45 + 1.1 × ln(H))

II.  AGB = AGB=0.04 x DBH^2.42 x H^1.125


Leaded to:
AGB = 0.01346 x H^3.787

Finally, to calculate carbon stocks (C) in above-ground biomass from trees, often the following formula is taken making use of a carbon fraction (CF) of 0.5:

C = AGB x CF = 0.5 x AGB

## Sources

### Data Sources

DTM, DSM and map of National Park's roads: https://www.geoportal.nrw/

Sentinel-2 satellite image bands: https://browser.dataspace.copernicus.eu/

### Scientific Sources

Chave, J., Réjou-Méchain, M., Búrquez, A., Chidumayo, E., Colgan, M. S., Delitti, W. B., ... & Vieilledent, G. (2014). Improved allometric models to estimate the aboveground biomass of tropical trees. Global Change Biology, 20(10), 3177–3190.

Cienciala, E., Černý, M., Apltauer, J., & Exnerová, Z. (2005). Biomass functions applicable to European beech. Journal of Forest Science, 51(4), 147–154.

Intergovernmental Panel on Climate Change (IPCC). (2006). 2006 IPCC Guidelines for National Greenhouse Gas Inventories, Vol. 4: Agriculture, Forestry and Other Land Use.

Pretzsch, H. (2009). Forest Dynamics, Growth and Yield: From Measurement to Model. Springer-Verlag Berlin Heidelberg.
ISBN: 978-3-540-88306-7
DOI: 10.1007/978-3-540-88307-4

Repola, J. (2009). Biomass equations for Scots pine and Norway spruce in Finland. Silva Fennica, 43(4), 625–647.
