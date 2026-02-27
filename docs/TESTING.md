# TESTING.md

## Target Applications

### Monsters

- [Apache NetBeans IDE](https://netbeans.apache.org/)
- [IntelliJ IDEA Community Edition](https://www.jetbrains.com/idea/download/)

### Minis

- [Apache JMeter](https://jmeter.apache.org/)
- [Freemind](https://sourceforge.net/projects/freemind/)

## Test Sessions

### General Recommendations

When testing, exercise these UI patterns:

- Expand deeply nested panels -> Very deep tree paths
- Open dialogs -> New windows with subtrees
- Menus + popups -> Bonus nodes generated on demand
- Dragged panels -> Dynamic structure changes

These all expose edge cases

### Concrete Suggestions

- Hover-highlight elements like:
  - menu items
  - toolbar buttons
  - tree rows
  - table cells
  - dock titles
  - tab headers
- Generate selectors for:
  - repeated components
  - dynamically indexed elements
  - unnamed shapes
- Refresh while changing underlying UI (example: opening a dialog mid-refresh)

### Quick Setup

1. Install NetBeans IDE
2. Open a large project (so the UI populates all panels)
3. Use your tool to inspect:
    - Explorer view
    - Properties windows
    - Output windows
    - Toolbars
    - Menus
    - Dialogs
4. Click deeply nested nodes and verify:
    - highlighting
    - selector output
    - tree performance
