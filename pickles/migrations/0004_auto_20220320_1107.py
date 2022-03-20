# Generated by Django 4.0.3 on 2022-03-20 16:07
from django.db import migrations
from pickles.models import Pickle

def seed_pickles(apps, schema_editor):
    pickles = [
        ("Ahold", "Ahold Pickle Chips Hamburger Dills"),
        ("The Brinery", "The Brinery Pickles Jape Kin Cod"),
        ("Marco Polo", "Marco Polo Home Made Pickled Mushrooms"),
        ("Woodstock", "Woodstock Organic Kosher Dill Pickles Deli Style"),
        ("Ahold", "Ahold Sauerkraut"),
        ("Vlasic", "Vlasic Stackers Bread & Butter Pickles"),
        ("Bell-view", "Bell-view Dill Pickles"),
        ("Ba-tampte", "Ba-tampte Half Sour Pickles"),
        ("Miss Jenny's", "Miss Jenny's Gluten-free Bread & Butter Pickles"),
        ("Silver Floss", "Silver Floss Shredded Sauerkraut"),
        ("Snyder Of Berlin", "Snyder Of Berlin Vlasic Dill Pickle Potato Chips"),
        ("Silver Floss", "Silver Floss Shredded Sauerkraut"),
        ("San Marcos", "San Marcos Pickled Sliced Carrots"),
        ("Deep", "Deep Lime Pickle Sweet"),
        ("Vlasic", "Vlasic Kosher Dill Pickle Spears"),
        ("Lay's", "Lay's Potato Chips Dill Pickle"),
        ("Ahold", "Ahold Shredded Sauerkraut"),
        ("The Brinery", "The Brinery Kimchi Oh Gee"),
        ("Mrs. Wages", "Mrs. Wages Kosher Dill Pickles Quick Process Pickle Mix"),
        ("Aunt Nellie's", "Aunt Nellie's Pickled Beets Whole"),
        ("Ahold", "Ahold Sliced Pickled Beets"),
        ("Boar's Head", "Boar's Head Kosher Dill Pickle Spears"),
        ("Deep", "Mango Titbit (sweet) Katki Pickle"),
        ("Ball", "Ball Bread & Butter Pickle Mix"),
        ("B&g", "B&g Pickle Chips Bread & Butter"),
        ("Puckered Pickle", "Puckered Pickle Co. Kosher Dill Pickle Spears"),
        ("Goya", "Goya Chiles Manzanos Pickled Manzano Peppers"),
        ("Vlasic", "Vlasic Stackers Kosher Dill Pickles"),
        ("Boar's Head", "Boar's Head Sauerkraut"),
        ("Othentic", "Othentic Organic Sauerkraut"),
        ("Bell-view", "Bell-view Sweet Pickles"),
        ("Farm Rich", "Farm Rich Crispy Dill Pickles Breaded Dill Pickle Slices"),
        ("The Brinery", "The Brinery Sauerkraut Stimulus Package"),
        ("Vlasic", "Vlasic Kosher Dill Whole Pickles"),
        ("Ahold", "Ahold Shredded Sauerkraut"),
        ("Reese", "Reese Pickled Whole Baby Corn"),
        ("Aunt Nellie's", "Aunt Nellie's Whole Pickled Baby Beets"),
        ("Ahold", "Ahold Pickle Chips Hamburger Dill"),
        ("Ahold", "Ahold Pickles Whole Sweet Gherkins No Sugar Added"),
        ("Ahold", "Ahold Pickle Chips Kosher Dills"),
        ("Mrs. Wages", "Mrs. Wages Dill Pickles Quick Process Pickle Mix"),
        ("Vlasic", "Vlasic Reduced Sodium Kosher Dill Spears Pickles"),
        ("Cains", "Cains Reduced Sodium Hamburger Pickle Chips"),
        ("Simply Asia", "Simply Asia Singapore Street Noodles Kimchi"),
        ("Bell-view", "Bell-view Polish Pickles Dill"),
        ("Vlasic", "Vlasic Kosher Dill Pickle Spears"),
        ("Giuliano", "Giuliano Specialty Italian Style Dill Pickles"),
        ("Woodstock", "Woodstock Organic Bread & Butter Pickles"),
        ("Claussen", "Claussen Deli-style Hearty Garlic Whole Pickles"),
        ("Greenwood", "Greenwood Whole Pickled Beets Sweet & Tangy"),
        ("Bubbies", "Pickle Dill Pure Koshr"),
        ("Burpee", "Burpee Cucumber Picklebush"),
        ("Sabrett", "Sabrett Sauerkraut"),
        ("Bell-view", "Bell-view Cauliflower Hot Pickled"),
        ("Cains", "Cains No Sugar Sugar Free Sweet Pickle Relish"),
        ("Osem", "Osem Mediterranean Pickles"),
        ("Vlasic", "Vlasic Sweet Pickle Relish"),
        ("Ahold", "Ahold Whole Pickles Kosher Dill"),
        ("Nongshim", "Nongshim Bowl Noodle Soup Spicy Kimchi"),
        ("Goya", "Goya Pickled Sliced Carrots"),
        ("Sushi Chef", "Sushi Chef Pickled Ginger"),
        ("Mrs. Fanning's", "Mrs. Fanning's The Original Bread 'n Butter Pickles"),
        ("Kissling's", "Kissling's Sauerkraut"),
        ("Giuliano", "Pickle Chptle Swt Smky"),
        ("King's", "King's Kimchi Korean Marinated Cabbage Mild"),
        ("Scrumptious Pantry", "Scrumptious Pantry Heirloom Pickles Beaver Dam Peppers"),
        ("Ahold", "Ahold Whole Pickles Kosher Baby Dill"),
        ("Greenwood", "Greenwood Sweet & Tangy Sliced Pickled Beets"),
        ("Libby's", "Libby's Crispy Sauerkraut Jumbo-can"),
        ("Vlasic", "Vlasic Bread & Butter Pickle Chips"),
        ("Bell-view", "Bell-view Fancy Pickled Sweet Beets"),
        ("Vlasic", "Vlasic Reduced Sodium Kosher Dill Stackers Pickles"),
        ("Del Monte", "Del Monte Seasoned Vegetables Pickled Green Beans With Dill Flavor"),
        ("B&g", "B&g New York Deli Style Pickles"),
        ("Ahold", "Ahold Pickle Spears Polish Dills"),
        ("Ball", "Ball Kosher Dill Pickle Mix"),
        ("Claussen", "Claussen Premium Sweet Pickle Relish"),
        ("Vlasic", "Vlasic Kosher Dill Whole Pickles"),
        ("Mt. Olive", "Mt. Olive Bread & Butter Pickles Old-fashioned Sweet"),
        ("Pringles", "Pringles Xtra Potato Crisps Screamin' Dill Pickle"),
        ("Aunt Nellie's", "Aunt Nellie's Pickled Beets Sliced"),
        ("Boar's Head", "Boar's Head Pickle & Pepper Loaf"),
        ("The Brinery", "The Brinery Sauerkraut Storm Cloud Zapper"),
        ("The Brinery", "The Brinery Sauerkraut Fair N' By"),
        ("Miss Jenny's", "Miss Jenny's Habanero Bread & Butter Pickles"),
        ("Ahold", "Ahold Pickle Spears Bread & Butter No Sugar Added"),
        ("Ahold", "Ahold Pickle Chips Bread & Butter"),
        ("Deep", "Deep Amba Haldar Pickle"),
        ("Lancaster Canning Company", "Lancaster Canning Company Pickled Sweet Baby Beets"),
        ("Scrumptious Pantry", "Scrumptious Pantry Heirloom Pickles Bread & Butter Style Cucumbers"),
        ("Lesserevil", "Lesserevil Dill Pickle Chia Crisps Gluten-free"),
        ("Ahold", "Ahold Whole Pickles Sweet Gherkins"),
        ("Greenwood", "Greenwood Sliced Pickled Beets Sweet & Tangy"),
        ("Ahold", "Ahold Shredded Sauerkraut"),
        ("Vlasic", "Vlasic Ovals Hamburger Dill Pickle Chips"),
        ("Cosmo's", "Cosmo's Pickled Eggs"),
        ("Vlasic", "Vlasic Kosher Dill Baby Whole Pickles"),
        ("Silver Floss", "Silver Floss Shredded Sauerkraut"),
        ("Mrs. Wages", "Mrs. Wages Bread & Butter Pickles Quick Process Pickle Mix"),
        ("Bubbies", "Pickle Chip Brd & Bttr"),
        ("Scrumptious Pantry", "Scrumptious Pantry Heirloom Pickled Vegetable Lemon Cucumbers"),
        ("Cains", "Cains Sugar Free Sweet B&b Pickle Chips"),
        ("Puckered Pickle", "Puckered Pickle Co. Natural Spicy Sweet Relish"),
        ("Giuliano", "Pickle Dill Hot Jlpno"),
        ("Loeb's", "Loeb's Pickle Crunch"),
        ("Nabisco", "Nabisco Wheat Thins Snacks Dill Pickle"),
        ("Famous Dave's", "Famous Dave's Pickle Chips Signature Spicy"),
        ("Suckerpunch", "Suckerpunch Pickles Spicy Garlic Originals"),
        ("Ball", "Ball Bread & Butter Pickle Mix"),
        ("Van Holten's", "Van Holten's Dill Pickle Hearty Dill"),
        ("Ball", "Ball Kosher Dill Pickle Mix"),
        ("Sabrett", "Sabrett Sauerkraut"),
        ("Lowell Foods", "Lowell Foods Old Country Style Polish Dill Pickles"),
        ("Kuhne", "Kuhne Traditional German Barrel Sauerkraut"),
        ("Mrs. Fanning's", "Mrs. Fanning's Bread'n Butter Pickles"),
        ("Vlasic", "Vlasic Bread & Butter Pickle Chips"),
        ("Lay's", "Lay's Dill Pickle Flavored Potato Chips"),
        ("Miss Jenny's", "Miss Jenny's Signature Salt & Pepper Pickles"),
        ("Vlasic", "Vlasic Stackers Kosher Dill Pickles"),
        ("Boar's Head", "Boar's Head Kosher Dill Whole Pickles"),
        ("Ahold", "Ahold Pickle Spears Kosher Dill"),
        ("Ahold", "Ahold Sauerkraut"),
        ("B&g", "B&g Gherkins Sweet Pickles"),
        ("Boar's Head", "Boar's Head Sauerkraut"),
        ("Vlasic", "Vlasic Sweet Gherkin Pickles"),
        ("Lowell Foods", "Lowell Foods Dill Pickles With Sliced Peppers"),
        ("Del Monte", "Del Monte Specialties Crinkle Cut Pickled Beets"),
        ("Ahold", "Ahold Pickle Spears Kosher Dills"),
        ("Talk O' Texas", "Talk O' Texas Okra Pickles Crips Mild"),
        ("Silver Floss", "Silver Floss Shredded Sauerkraut"),
        ("Scrumptious Pantry", "Scrumptious Pantry Heirloom Pickles Red Beets With Fresh Thyme"),
        ("Ahold", "Ahold Whole Pickles Sweet Midget"),
        ("Giuliano", "Pickle Dill Kosher Zesty"),
        ("Woodstock", "Woodstock Organic Kosher Dill Pickles Sliced"),
        ("Ahold", "Ahold Whole Pickle Kosher Baby Dills"),
        ("Kuhne", "Kuhne Pickled Red Cabbage"),
        ("Mcclure's", "Mcclure's Kettle Cooked Potato Chips Garlic Dill Pickle"),
        ("Farm Rich", "Farm Rich Crispy Dill Pickles"),
        ("Woodstock", "Woodstock Organic Bite-sized Kosher Baby Dill Pickles"),
        ("Bell-view", "Bell-view Dill Kosher Pickles"),
        ("Hatfield", "Hatfield Old Fashioned Sauerkraut"),
        ("Claussen", "Claussen Easy Squeeze Sweet Pickle Relish"),
        ("Grillo's Pickles", "Grillo's Pickles Italian Dills Hot"),
        ("Lowell Foods", "Lowell Foods Polish Dill Pickles With Sweet Peppers"),
        ("Oscar Mayer", "Oscar Mayer Pickle & Pimiento Loaf"),
        ("Vlasic", "Vlasic Kosher Dill Baby Whole Pickles"),
        ("Ahold", "Ahold Pickles Whole Kosher Dill"),
        ("Bell-view", "Bell-view Cauliflower Hot Pickled"),
        ("A-grosik", "A-grosik Dill Pickles In Brine All Natural"),
        ("Cains", "Cains Sweet Pickle Relish"),
        ("Ahold", "Ahold Pickle Chips Bread & Butter"),
        ("Cains", "Cains Balasamic Munchers Pickles"),
        ("Old El Paso", "Old El Paso Pickled Jalapeno Slices"),
        ("Ahold", "Ahold Bread & Butter Pickle Chips No Sugar Added"),
        ("Wildbrine", "Sauerkraut Dill & Grlc"),
        ("Wildbrine", "Sauerkraut Arame & Gngr"),
        ("Wildbrine", "Sauerkraut Curry & Clflwr"),
        ("Wildbrine", "Sauerkraut Beet & Cabbage"),
        ("Wildbrine", "Horseradish Kimchi Miso"),
        ("Wildbrine", "Kimchi Korean"),
        ("Wildbrine", "Kimchi Thai"),
        ("Wildbrine", "Pickle Slc Dill"),
        ("King Crunch", "Pickle Dill Spear Kosher"),
        ("Wonderfully Raw", "Snip Chip Dill Pickle Org"),
        ("Gefen", "Pickle Sliced"),
        ("Krakus", "Sauerkraut & Carrot"),
        ("Krakus", "Sauerkraut"),
        ("Krakus", "Pickle Dill Polish"),
        ("Ricks Picks", "Pickle K O  Org"),
        ("Kasias", "Pierogi Sauerkraut"),
        ("Annie Chuns", "Soup Bowl Kimchi"),
        ("Crosse & Blackwell", "Branston Pickle Orgnl"),
        ("Paldo", "Noodle Bowl Kimchi"),
        ("Othentic", "Pickle Dill Polish"),
        ("Othentic", "Pickle Dill Spear Swt & S"),
        ("Othentic", "Sauerkraut Alntrl"),
        ("Othentic", "Pickle Dill Polish Org"),
        ("Othentic", "Pickle Jewish Deli Styl Org"),
        ("Othentic", "Pickle Spear Swt&spcy Org"),
        ("Biotta", "Juice Sauerkraut"),
        ("Crosse & Blackwell", "Branston Pickle"),
        ("Ricks Picks", "Bean Grn Mean Pickled"),
        ("Ricks Picks", "Beet Phat Pickled"),
        ("Ricks Picks", "Smokra Pickled"),
        ("Conscious Choice", "Pickle Beer Orgnl"),
        ("Ba Tampte", "Sauerkraut Jar"),
        ("Ba Tampte", "Sauerkraut Cello"),
        ("Ba Tampte", "Pickle Half Sour"),
        ("Conscious Choice", "Pickle Dill Frances Cellar"),
        ("Conscious Choice", "Pickle Dill Harold Purdy Hot"),
        ("Conscious Choice", "Pickle Dill Harold Dern Hot"),
        ("Boscoli", "Asparagus Spicy Pickled"),
        ("Boscoli", "Garlic Spicy Pickled"),
        ("Boscoli", "Bean Spicy Pickled"),
        ("A Grosik", "Pickle Polish Dill"),
        ("A Grosik", "Sauerkraut"),
        ("A Grosik", "Pickle Gherkin"),
        ("A Grosik", "Pickle Polish Dill"),
        ("Wickles", "Pickle Orgnl"),
        ("Othentic", "Sauerkraut"),
        ("Bigs", "Seed Snflwr Vlasic Dill Pickle"),
        ("Puckered Pickle", "Pickle Spears 300pc"),
        ("Ricks Picks", "Pickle Peoples Grlc Dill"),
        ("Ricks Picks", "Pickle Classic Sours"),
        ("Lynnaes Gourmet", "Pickle Chip"),
        ("Lynnaes Gourmet", "Pickle Chip Hot Mama"),
        ("Lynnaes Gourmet", "Pickle Spear Hot Mama"),
        ("Puckered Pickle", "Pickle Spear Spcy Deli"),
        ("Martha Stewart", "Pickle Spear Snckng"),
        ("Martha Stewart", "Pickle Chip Zesty Hot"),
        ("Martha Stewart", "Okra Pickled"),
        ("Martha Stewart", "Pickle Chip Bread&bttr"),
        ("Kuhne", "Pickle Sandwich Slices"),
        ("Kuhne", "Pickle Gherkin Grmt Premi"),
        ("Del Monte", "Pickle Clsc Bread & Bttr"),
        ("Del Monte", "Pickle Chunk Hot&swt"),
        ("Del Monte", "Pickle Dill Grndma Baby"),
        ("Del Monte", "Pickle Spear Kshr Dill Gr"),
        ("Del Monte", "Pickle Chunk Dill Grlc"),
        ("Food Should Taste Good", "Chip Tortla Kimchi"),
        ("Liebers", "Pickle Dill"),
        ("Liebers", "Pickle Gehrkin Dill"),
        ("Galil", "Pickle 7-9 Xvngr"),
        ("Sechlers", "Pickle Candied Swt Apple"),
        ("Sechlers", "Pickle Swt Mixed Heat"),
        ("Mrs Wages", "Pickle Barrel Dsp 72pc"),
        ("Pataks", "Pickled Garlic"),
        ("Franks", "Sauerkraut Sngl Dsp 144pc"),
        ("Puckered Pickle", "Pickle Spear Kosher"),
        ("Puckered Pickle", "Pickle Whole Baby Dill"),
        ("Bubbies", "Pickle Relish Kosher Dill"),
        ("Cracovia", "Pickle Dill Polish"),
        ("Cracovia", "Sauerkraut"),
        ("Osem", "Pickle Meditern 18-25"),
        ("Dolores", "Pork Rinds Pickled"),
        ("Dolores", "Pigs Feet Pickled"),
        ("Tillen Farms", "Asparagus Pickled"),
        ("Franks", "Sauerkraut Hot Dog Dsp 54pc"),
        ("Franks", "Sauerkraut Juice"),
        ("Mrs Wages", "Mix Pickle 4flvr Dsp 72pc"),
        ("Pataks", "Relish Pickled Mixed"),
        ("Hengstenberg", "Pickle Polish"),
        ("Pataks", "Pickled Brinjal"),
        ("Tiffes", "Okra Pickled Mild"),
        ("Tiffes", "Okra Pickled Hot"),
        ("Hengstenberg", "Pickle Gherkin Knax"),
        ("Nong Shim", "Noodle Inst Kimchi Ramyun"),
        ("Osem", "Pickle Meditern 7-9"),
        ("Galil", "Pickle Cucumber 18-25"),
        ("Galil", "Pickle Cucumber 7-9"),
        ("Cracovia", "Beets Baby Pickled"),
        ("Cracovia", "Sauerkraut With Carrot"),
        ("Ba Tampte", "Sauerkraut Cello"),
        ("Miss Jennys Pickles", "Pickle Salt & Pppr Jlpno"),
        ("Tony Packos", "Packo Thin Slcd Pickles &"),
        ("Tony Packos", "Pickle & Pepper Orig"),
        ("Tony Packos", "Pickle Ppr Swt Hot"),
        ("Roland", "Pickle Dill Chip"),
        ("Talk O Texas", "Okra Pickled Hot"),
        ("Tony Packos", "Packo Pickle & Pepper Rel"),
        ("Kuhne", "Pickle Garlic Barrel"),
        ("Santa Barbara", "Asparagus Pickled Hot"),
        ("Franks", "Sauerkraut Can"),
        ("Conscious Choice", "Pickle Sissy Swt Harolds"),
        ("Mrs Wages", "Mix Pickle Med Spcy"),
        ("Mrs Wages", "Mix Pickle Brd N Btr Zsty"),
        ("Manischewitz", "Sauerkraut Po"),
        ("Ziyad", "Turnip Pickled"),
        ("Sechlers", "Pickle Brd & Btr Zsty Chnk"),
        ("Kuhne", "Sauerkraut Barrel"),
        ("Hengstenberg", "Pickle Gherkin Knax Lrg"),
        ("Pataks", "Pickled Mango Xhot"),
        ("Pataks", "Pickled Chile"),
        ("Hengstenberg", "Sauerkraut Bavarian"),
        ("Kuhne", "Pickle Barrel"),
        ("Franks", "Sauerkraut Can"),
        ("Pataks", "Pickled Lime Mild"),
        ("Pataks", "Pickled Mango Medm"),
        ("Tabasco", "Pickle Hot & Sweet"),
        ("Tabasco", "Okra Pickled Spicy"),
        ("Sechlers", "Pickle Swt Diced Salad"),
        ("Sechlers", "Pickle Candied Swt Mix"),
        ("Sechlers", "Pickle Candied Swt Orng Strip"),
        ("Sechlers", "Pickle Candied Swt Dill Strip"),
        ("Sechlers", "Pickle Swt"),
        ("Sechlers", "Relish Pickle Swt"),
        ("Sechlers", "Relish Dill Pickle"),
        ("Sechlers", "Pickle Chip Med Swt"),
        ("Sechlers", "Pickle Candied Swt Mixed"),
        ("Sechlers", "Pickle Candied Swt Raisin"),
        ("Sechlers", "Pickle Dill Genuine No Grlc"),
        ("Sechlers", "Pickle Candied Swt Gherkin"),
        ("Sechlers", "Pickle Candied Swt Orng Chnks"),
        ("Sechlers", "Pickle Brd & Btr Slice"),
        ("Marquis", "Pickle Gherkin"),
        ("Sechlers", "Pickle Cndyd Swt Dill Chn"),
        ("Van Holtens", "Pickle Dill Mild"),
        ("Van Holtens", "Pickle Dill King Sz"),
        ("Amish Wedding", "Beet Pickled Baby"),
        ("Amish Wedding", "Pickle Bread & Butter"),
        ("Bubbies", "Sauerkraut"),
        ("Ba Tampte", "Tomato Pickled"),
        ("Ba Tampte", "Sauerkraut Jar"),
        ("Ba Tampte", "Pickle Bread & Butter"),
        ("Ba Tampte", "Pickle Deli Whole"),
        ("Ba Tampte", "Pickle Deli Halve"),
        ("Mrs Wages", "Mix Pickle 6flvr Dsp 80pc"),
        ("Van Holtens", "Pickle Hot Dill"),
        ("Van Holtens", "Pickle Sour Dill"),
        ("Van Holtens", "Pickle Kosher Deli"),
        ("Van Holtens", "Pickle Hot Mama"),
        ("Ba Tampte", "Pickle Garlic Dill"),
        ("Franks", "Sauerkraut Sngl")
    ]
    for (maker, name) in pickles:
        p = Pickle(name=name, maker=maker)
        p.save()

class Migration(migrations.Migration):
    dependencies = [
        ('pickles', '0003_pickle_maker'),
    ]

    operations = [
        migrations.RunPython(seed_pickles)
    ]
