import pygame
import random

class Sorting:
    def __init__(self, size, fps):
        self.fps = fps
        self.size = size
        self.createUnsortedList()
        self.sorted = False
        self.algorithms = ["BubbleSort", "SelectionSort", "QuickSort", "CombSort", "CocktailSort"]
        self.algorithm = None
        self.timer = 0
        self.complexity = None
        self.length = len(self.unsortedList)

    def createUnsortedList(self):
        self.sorted = False
        self.unsortedList = [i for i in range(1, self.size + 1)]
        random.shuffle(self.unsortedList)

    def selectScreen(self):
        self.createUnsortedList()
        font = pygame.font.Font(None, 180)
        screen.fill("black")

        # Select
        text = font.render("Select:", True, "green")
        screen.blit(text, (30, 20))

        y = 170
        number = 1
        font = pygame.font.Font(None, 100)

        for alg in self.algorithms:
            text = font.render(str(number) + ". " + alg, True, "green")
            screen.blit(text, (40, y))
            number += 1
            y += 100

        pygame.display.flip()

        while True:
            # Fenster Schließen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.fps = 360
                        self.BubbleSort()
                    elif event.key == pygame.K_2:
                        self.fps = 30
                        self.SelectionSort()
                    elif event.key == pygame.K_3:
                        self.fps = 90
                        self.QuickSort()
                    elif event.key == pygame.K_4:
                        self.fps = 90
                        self.CombSort()
                    elif event.key == pygame.K_5:
                        self.fps = 360
                        self.CocktailShakerSort()

    def displaySorting(self):
        font = pygame.font.Font(None, 70)

        # Fenster Schließen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        x = 100
        screen.fill("black")

        # Name und Zeit darstellen
        text = font.render(self.algorithm + ": " + str(self.timer), True, "green")
        screen.blit(text, (30, 20))

        # Komplexität in Big O Notation Darstellen
        text = font.render(self.complexity, True, "green")
        screen.blit(text, (250, 630))

        # jedes Element der Liste als Rechteck darstellen
        for height in self.unsortedList:
            pygame.draw.rect(screen, (0, 255, 0), (x, 600 - height * 5, 5, height * 5))
            x += 5

        pygame.display.flip()
        self.timer = (pygame.time.get_ticks() - self.start_tick) / 1000
        clock.tick(self.fps)

    def BubbleSort(self):
        self.start_tick = pygame.time.get_ticks()
        self.complexity = "O(n^2)"
        self.algorithm = "BubbleSort"

        if not self.sorted:
            for i in range(self.length):
                for j in range(self.length - i - 1):
                    if self.unsortedList[j] > self.unsortedList[j + 1]:
                        self.unsortedList[j], self.unsortedList[j + 1] = self.unsortedList[j + 1], self.unsortedList[j]
                        self.displaySorting()
            self.sorted = True

        pygame.time.wait(1500)
        self.selectScreen()

    def SelectionSort(self):
        self.start_tick = pygame.time.get_ticks()
        self.algorithm = "SelectionSort"
        self.complexity = "O(n^2)"

        if not self.sorted:
            for i in range(self.length - 1):
                min_idx = i
                for j in range(i + 1, self.length):
                    if self.unsortedList[min_idx] > self.unsortedList[j]:
                        min_idx = j
                self.unsortedList[i], self.unsortedList[min_idx] = self.unsortedList[min_idx], self.unsortedList[i]
                self.displaySorting()
            self.sorted = True

        pygame.time.wait(1500)
        self.selectScreen()

    def QuickSort(self):
        self.start_tick = pygame.time.get_ticks()
        self.algorithm = "QuickSort"
        self.complexity = "O(n log n)"

        def partition(low, high):
            pivot = self.unsortedList[high]
            i = low - 1
            for j in range(low, high):
                if self.unsortedList[j] < pivot:
                    i += 1
                    self.unsortedList[i], self.unsortedList[j] = self.unsortedList[j], self.unsortedList[i]
                    self.displaySorting()
            self.unsortedList[i + 1], self.unsortedList[high] = self.unsortedList[high], self.unsortedList[i + 1]
            self.displaySorting()
            return i + 1

        def quickSortHelper(low, high):
            if low < high:
                pi = partition(low, high)
                quickSortHelper(low, pi - 1)
                quickSortHelper(pi + 1, high)

        if not self.sorted:
            quickSortHelper(0, self.length - 1)
            self.sorted = True
            pygame.time.wait(1500)
            self.selectScreen()

    def CocktailShakerSort(self):
        self.start_tick = pygame.time.get_ticks()
        self.algorithm = "CocktailShakerSort"
        self.complexity = "O(n^2)"

        n = len(self.unsortedList)
        swapped = True

        while swapped:
            swapped = False

            for i in range(n - 1):
                if self.unsortedList[i] > self.unsortedList[i + 1]:
                    self.unsortedList[i], self.unsortedList[i + 1] = self.unsortedList[i + 1], self.unsortedList[i]
                    swapped = True
                    self.displaySorting()

            if not swapped:
                break

            swapped = False
            for i in range(n - 1, 0, -1):
                if self.unsortedList[i] < self.unsortedList[i - 1]:
                    self.unsortedList[i], self.unsortedList[i - 1] = self.unsortedList[i - 1], self.unsortedList[i]
                    swapped = True
                    self.displaySorting()
        pygame.time.wait(1500)
        self.selectScreen()

    def CombSort(self):
        self.start_tick = pygame.time.get_ticks()
        self.algorithm = "CombSort"
        self.complexity = "O(n^2)"

        gap = self.length
        shrink_factor = 1.3
        sorted = False

        while gap > 1 or not sorted:
            gap = int(gap / shrink_factor)
            if gap < 1:
                gap = 1
            sorted = True

            i = 0
            while i + gap < self.length:
                if self.unsortedList[i] > self.unsortedList[i + gap]:
                    self.unsortedList[i], self.unsortedList[i + gap] = self.unsortedList[i + gap], self.unsortedList[i]
                    sorted = False
                    self.displaySorting()
                i += 1

        pygame.time.wait(1500)
        self.selectScreen()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()
running = True

List = Sorting(100, 60)
List.selectScreen()
