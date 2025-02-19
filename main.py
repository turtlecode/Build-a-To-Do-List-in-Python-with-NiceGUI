from nicegui import ui

tasks = []

def add_task(task_name):
    if task_name:
        tasks.append({"name": task_name, "done": False})
        update_task_list()

def toggle_task(index):
    tasks[index]["done"] = not tasks[index]["done"]
    update_task_list()

def update_task_list():
    task_container.clear()
    with task_container:
        for i, task in enumerate(tasks):
            with ui.row():
                ui.checkbox(task["name"], value=task["done"], on_change=lambda e, i=i: toggle_task(i))
                ui.button("❌", on_click=lambda i=i: remove_task(i), color="red")

def remove_task(index):
    del tasks[index]
    update_task_list()

ui.label("To-Do List").classes("text-2xl font-bold")
task_input = ui.input(placeholder="Enter a task").props("autofocus")
ui.button("Add", on_click=lambda: add_task(task_input.value))

task_container = ui.column()

ui.run()