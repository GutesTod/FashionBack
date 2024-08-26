from pydantic import BaseModel, Field

class CategoryBase(BaseModel):
    name: str = Field(..., description="Название категории")

    class Config:
        orm_mode = True

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int