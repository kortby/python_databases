from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+mysqlconnector://root@localhost:3306/household', echo=True)
Base = declarative_base()


class Project(Base):
    __tablename__ = 'projects'
    __table_args__ = {'schema': 'household'}

    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=255))

    def __repr__(self):
        return f'<Project(title="{self.title}", description="{self.description}")'


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'schema': 'household'}

    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('household.projects.project_id'))
    description = Column(String(length=255))

    project = relationship('Project')

    def __repr__(self):
        return f'<Task(description="{self.description}")'


Base.metadata.create_all(engine)

session_maker = sessionmaker()

# session allow as to work with database
session_maker.configure(bind=engine)
session = session_maker()

organize_project_closet = Project(
    title='Organize closet', description='Organize closet by color and style')

session.add(organize_project_closet)
session.commit()


tasks = [
    Task(project_id=organize_project_closet.project_id,
         description='Cleaning the floor with new products'),
    Task(project_id=organize_project_closet.project_id,
         description='Hiding winter clothes'),
    Task(project_id=organize_project_closet.project_id,
         description='Painting the room with couple of colors'),
]

session.bulk_save_objects(tasks)
session.commit()

our_project = session.query(Project).filter_by(title='Organize closet').first()

print('------------------------------------')
print(our_project)
print('------------------------------------')
our_tasks = session.query(Task).all()
print(our_tasks)
